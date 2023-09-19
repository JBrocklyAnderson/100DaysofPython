import os, datetime
from replit import db

# screen-clearing function
def clearScreen():
  os.system("cls" if os.name == "nt" else "clear")

def clear():
  # clearScreen()
  while True:
    confirm = input("Are you sure you want to clear your whistles? Yes/No\n\n")
    if confirm == "yes": 
      keys = db.keys() ## get all keys
      for key in keys:
        del db[key] ## delete all keys in for loop
      print("\nWhistles successfully cleared.")
    else:
      return False

def add():
  clearScreen()
  timestamp = datetime.datetime.now() ## timestamp the Whistles
  whistle = input("What's on your mind?\n\n")
  db[timestamp] = whistle ## set timestamp as they key and append the Whistle to the database
  clearScreen()

# define a viewing function
def view(start = 0): ## set the function to start at index 0
  clearScreen()
  whistles = list(sorted(db.keys(), reverse = True))[start:start + 10] ## convert the keys into a list, sort them, and splice the first ten
  
  for whistle in whistles:
    print(f"\033[36m{whistle}\033[0m: {db[whistle]}\n") ## colorcode Whistles
  while True: 
    direction = input("Next (n) / Previous (p) / Back (b)?\n\n").strip().lower() ## submenu options
    if direction == "n":
      if len(whistles) == 10: # as long as there are 10 more Whistles to display
        return view(start + 10)
      else:
        print("\nYou have no more Whistles to hum about.\n")
    elif direction == "p":
      if start == 0: 
        print("\nThese are your most recent Whistles.\n")
        continue
      return view(start - 10) # index backwards so long as the user isn't viewing the most recent Whistles
      print("\nYou have no more Whistles to hum about.\n")
    elif direction == "b":
      return
    else:
      print("\nInvalid option. Please try again.\n")

while True:
  clearScreen()
  print("Whistler\nA Twitter for One\n")
  menu = input("1. Add Whistle\n2. View Timeline\n3. Stop Whistling\n4. Clear Timeline\n\n").strip()
  if menu == "1":
    add()
  elif menu == "2":
    view()
  elif menu == "3":
    clearScreen()
    break
  elif menu == "4":
    clear()
  