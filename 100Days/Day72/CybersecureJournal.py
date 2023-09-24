import os, time, random ## useful libraries
from datetime import datetime, timezone ## supporting datetime object manipulation and timestamping
from getpass import getpass as security ## hiding user input
from replit import db ## accessing the database

# screen-clearing function
def cls():
  os.system("cls" if os.name == "nt" else "clear") # clear screen on Windows ("nt") with "cls" or Linux/MacOS with "clear"

# subroutine used to "create account"
def newUser():
  global username
  global password
  salt = random.randint(1, 1000000) ## randomizing salt values
  saltedPW = f"{password}{salt}" ## appending the salt to chosen password
  hashed = hash(saltedPW) ## hashing the new password
  db[username] = {"password": hashed,
               "salt": salt,
               "journal": {}} ## storing this information in the database
  print(f"\nCongratulations {username}! Your account has been created successfully.")
  input("\nPress enter to continue...")


# function to add journal entries
def addEntry():
  cls()
  timestamp = datetime.now(timezone.utc).replace(microsecond = 0) ## timestamp the entries and ignore microsecond values 
  entry = input("What's on your mind?\n\n")
  db[username]["journal"][str(timestamp)] = entry ## set timestamp as they key and append the entry to the database
  print(f"\nEntry added successfully for \033[36m{timestamp}\033[0m!")
  time.sleep(3)
  cls()


# define viewing function
def viewJournal(start = 0): ## set the function to start at index 0
  cls()
  journal = db[username]["journal"] ## access the journal subdictionary in the database
  entries = list(sorted(journal.keys(), reverse = True))[start:start + 3] ## convert the keys into a list, sort them, and fetch the first three  

  if not entries:
    print("You have no journal entries")
    time.sleep(2)
    return
  
  viewType = input("Search (s) / Display Recent (r)\n\n").strip().lower()
  if viewType == "s": ## view by search
    cls()
    searchDate = input("What date would you like to search for? (YYYY-MM-DD)\n\n")
    matchingEntries = [key for key in journal if searchDate in key]
    
    if matchingEntries: ## assuming there are entries for the search date
      for entry in matchingEntries: ## grab the entries
        print(f"\033[36m{entry}\033[0m: {journal[entry]}\n") ## colorcode based on timestamp
        input("\nPress enter to return to main menu.")
    else:
      print(f"No entries were found for {searchDate}.")
      time.sleep(2)

  
  elif viewType == "r": ## view by recent
    cls()
    while True: 
      for entry in entries:
        print(f"\033[36m{entry}\033[0m: {journal[entry]}\n") ## colorcode timestamps
      direction = input("Next (n) / Previous (p) / Back (b)?\n\n").strip().lower() ## submenu options
      
      if direction == "n":
        cls()
        if len(entries) == 3: ## as long as there are 3 more entries to display
          start += 3 ## move the index forward
          entries = list(sorted(journal.keys(), reverse = True))[start:start + 3] ## update the variable to call new indices
        else:
          cls()
          print("These are your oldest entries.\n")
      elif direction == "p":
        if start == 0: ## so long as the user is viewing the most recent entries
          cls()
          print("These are your most recent entries.\n")
        else:
          cls()
          start -= 3 ## move the index backward
          entries = list(sorted(journal.keys(), reverse = True))[start:start + 3] ## update the variable to call new indices
      elif direction == "b":
        return
      else:
        cls()
        print("\nInvalid entry. Please try again.\n")
        time.sleep(2)
  
  else: ## handle invalid entry
    print("Invalid entry. Please try again.")
    time.sleep(2)

# function to wipe the journal
def clearJournal():
  cls()
  confirm = input("Are you absolutely sure you want to clear your journal? This will permanently erase everything and cannot be undone.\n\nYes/No\n\n").strip().lower() # confirmation to wipe the journal
  if confirm == "yes":
    while True:
      cls()
      print("Confirm password to clear journal.\n")
      
      PWask = security("Enter your password:   ").strip()
      if username in db: 
        salt = db[username]["salt"] ## grabbing salt value from specific user 
        saltedPW = f"{PWask}{salt}" ## appending registered salt value to their password guess
        hashPW = hash(saltedPW) ## hashing the new password
        if hashPW == db[username]["password"]: ## checking the hashed password-salt against database info
          db[username]["journal"] = {}
          print("\nJournal successfully cleared.")
          time.sleep(2)
          break
        else: 
          print("Incorrect password. Try again")
          time.sleep(2)
          break
      else:
        print("Authentification failed. Try again.") 
        time.sleep(2)
        break
  else:
    print("\nReturning to journal menu...")
    time.sleep(2)
    

# authenticating login information
def login(username, password):
  if username in db: 
    salt = db[username]["salt"] ## grabbing salt value from specific user if they already have an "account"
    saltedPW = f"{password}{salt}" ## appending registered salt value to their password guess
    hashPW = hash(saltedPW) ## hashing the new password

    if hashPW == db[username]["password"]: ## checking the hashed password-salt against info stored in the database
      print(f"\nLogin Successful! Welcome {username}.")
      time.sleep(2)
      return True
    else:
      print("\nLogin unsuccessful.\n")
      return False
  else:
    create = input("Username not found. Do you wish to create an account?\n\nYes/No\n\n").strip().lower()
    if create == "yes":
      newUser()
      return True
    else:
      print("\nPlease try again.")
      time.sleep(2)
      return False

# initial title screen
while True:
  cls()
  print("My Innermost Thoughts:\nA daily excursion into adventure and longing.\n")
  username = security("Enter your username:   ").strip()
  password = security("Enter your password:   ").strip()

  if login(username, password):
    break
  else:
    print("\nLogin unsuccessful. Try again.")
    time.sleep(2)
    


while True: ## main program loop
  cls()
  print("My Innermost Thoughts:\nA daily excursion into adventure and longing.\n")
  
  menu = input("1. Add Entry\n2. View Journal\n3. Clear Journal\n4. Close Journal\n\n")
  
  if menu == "1":
    addEntry()
  elif menu == "2":
    viewJournal()
  elif menu == "3":
    clearJournal()
  elif menu == "4":
    cls()
    print("Goodbye!")
    time.sleep(2)
    cls()
    break
  else:
    print("Invalid option. Please try again.")
    time.sleep(2)
    cls()