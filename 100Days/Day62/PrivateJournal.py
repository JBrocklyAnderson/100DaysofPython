""" This program currently uses UTC to timestamp journal entries. This limits the functionality of the view by search" function if the user and their operating system do not exist in the time zone. Theoretical improvements that I could make to this code include handling time zone differences between what the program stores as a timestamp and what the user inputs as their search date. This would require converting the search input found within the view function into a date object based on the user and their operating system's local time. This is beyond the scope of the challenge, but would be interesting to explore in the future. """

import os, time ## to support screen clearing and statements only needed for short duration
from datetime import datetime, timezone ## to support datetime object manipulation and timestamping
from getpass import getpass as security ## to support input authentification
from replit import db ## to support database management

# screen-clearing function
def clearScreen():
  os.system("cls" if os.name == "nt" else "clear") # clear screen on Windows ("nt") with "cls" or Linux/MacOS with "clear"

# function to add journal entries
def addEntry():
  clearScreen()
  timestamp = datetime.now(timezone.utc).replace(microsecond = 0) ## timestamp the entries and ignore microsecond values 
  entry = input("What's on your mind?\n\n")
  db[timestamp] = entry ## set timestamp as they key and append the entry to the database
  print(f"\nEntry added successfully for \033[36m{timestamp}\033[0m!")
  time.sleep(2.5)
  clearScreen()

# define viewing function
def viewJournal(start = 0): ## set the function to start at index 0
  clearScreen()
  entries = list(sorted(db.keys(), reverse = True))[start:start + 3] ## convert the keys into a list, sort them, and fetch the first three  
  
  viewType = input("Search (s) / Display Recent (r)\n\n").strip().lower() # take input before 
  
  if not entries: # make sure the journal has entries
      print("You have no journal entries.")
      return
    
  # view by search
  if viewType == "s":
    clearScreen()
    
    # get date to search for associated entries
    searchDate = input("View entries from which date (YYYY-MM-DD)?  ").strip()
    matchingEntries = list(db.prefix(searchDate))

    if matchingEntries: ## assuming there are entries for the search date
      for entry in matchingEntries: # grab the entries
        print(f"\033[36m{entry}\033[0m: {db[entry]}\n") ## colorcode based on timestamp
      input("\nPress enter to return to main menu.")
    else:
      print(f"No entries were found for {searchDate}.")
      time.sleep(2)

  # view all
  elif viewType == "r":
    clearScreen()
    while True: 
      for entry in entries:
        print(f"\033[36m{entry}\033[0m: {db[entry]}\n") ## colorcode timestamps
      direction = input("Next (n) / Previous (p) / Back (b)?\n\n").strip().lower() ## submenu options
      
      if direction == "n":
        clearScreen()
        if len(entries) == 3: ## as long as there are 3 more entries to display
          start += 3 ## move the index forward
          entries = list(sorted(db.keys(), reverse = True))[start:start + 3] ## update the variable to call new indices
        else:
          clearScreen()
          print("These are your oldest entries.\n")
      elif direction == "p":
        if start == 0: # so long as the user is viewing the most recent entries (`start = 1` would mean 1 more recent entry exists) 
          clearScreen()
          print("These are your most recent entries.\n")
        else:
          clearScreen()
          start -= 3 ## move the index backward
          entries = list(sorted(db.keys(), reverse = True))[start:start + 3] ## update the variable to call the first 3 indices
      elif direction == "b":
        return
      else:
        print("\nInvalid entry. Please try again.\n")
  
  # handle invalid entry
  else:
    print("Invalid entry. Please try again.")
    time.sleep(2)

# function to wipe the journal
def clearJournal():
  clearScreen()
  confirm = input("Are you absolutely sure you want to clear your journal? This will permanently erase everything and cannot be undone.\n\nYes/No\n\n").strip().lower() # confirmation to wipe the journal
  if confirm == "yes":
    print()
    if securityProtocol(): ## require username and password re-entry
      entries = db.keys() ## get all keys
      for entry in entries:
        del db[entry] ## delete all keys in for-loop
      print("\nDiary successfully erased.\n")
  else:
    return ## until the user gets it right

# authentification function
def securityProtocol():
  while True:
    userName = security("Enter username:  ").strip() # Asimov888
    passWord = security("Enter password:  ").strip() # 3Xtremely$ecure
    
    if userName == "Asimov888" and passWord == "3Xtremely$ecure":
      return True
    else:
      print("\nIncorrect username and password. Please try again.\n")

# initial title screen
print("My Innermost Thoughts:\nA daily excursion into adventure and longing.\n")

while not securityProtocol():
  print("Failed authentification protocol. Closing journal.")
  exit() 

# main program loop
while True:  
    clearScreen()
    print("My Innermost Thoughts:\nA daily excursion into adventure and longing.\n")
    menu = input("1. Add Entry\n2. View Journal\n3. Clear Journal\n4. Close Journal\n\n")
    if menu == "1":
      addEntry()
    elif menu == "2":
      viewJournal()
    elif menu == "3":
      clearJournal()
    elif menu == "4":
      clearScreen()
      print("Goodbye!")
      time.sleep(2)
      clearScreen()
      break
    else:
      print("Invalid option. Please try again.")
      time.sleep(2)
      clearScreen()