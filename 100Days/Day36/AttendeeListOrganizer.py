import os, time

# initialize empty list
people = []

# define a subroutine to keep the console clean
def clearScreen():
  os.system("cls" if os.name == "nt" else "clear")

# define a subroutine to print the list upon request
def printList():
  print("Current List of Attendees")
  print()
  for person in people:
    print(f"{person}")

while True:  
  # define menu options
  choice = input(
 """    View list? (v)
    Add name? (a)
    Edit name? (e)
    Remove name? (r)
    Clear names? (c)
    Exit list? (x)\n\n""")

  if choice == "v":
    clearScreen()
    printList()
    time.sleep(1)
    print()
    input("Press ENTER to continue...")
  
  # adding names 
  elif choice == "a":
    clearScreen()
    first = input("What's their first name?\n").strip().capitalize()
    print()
    last = input("What's their last name\n").strip().capitalize()
    
    # combine first and last names
    fullName = f"{first} {last}"
    
    # prevent duplicates
    if fullName not in people:
      people.append(fullName)
      clearScreen()
      printList()
      time.sleep(1)
      clearScreen()
    else:
      print()
      print(f"{fullName} is already in the attendee list.")
      input("Press ENTER to continue...")
      clearScreen()

  # editing names
  elif choice == "e":
    clearScreen()
    edit = input("Which attendee's name needs correcting?\n")
    if edit.strip().title() in people:
      print()
      newName = input("Their correct name:\n")
      # preventing duplicates
      if newName.strip().title() not in people:
        index = people.index(edit)
        people[index] = newName
        clearScreen()
      else:
        print(f"{newName} is already in the attendee list or you've capitalized their name incorrectly.")
        input("Press ENTER to continue...")
        clearScreen()
    else:
      print(f"{edit} doesn't seem to be on the list.")
      input("Press ENTER to continue...")
      clearScreen()
  
  # removing names
  elif choice == "r":
    clearScreen()
    remove = input("Who would you like to remove?\n")
    if remove.strip().title() in people:
      confirm = input(f"Are you sure you want to remove {remove.strip().title()}?\n")
      if confirm.strip().lower() == "yes":
        people.remove(remove.strip().title())
        clearScreen()
    else:
      print("There doesn't seem to be anybody here by that name.")
      input("Press ENTER to continue...")
      clearScreen()

  elif choice == "c":
    clearScreen()
    clear = input("Are you sure you wish to clear the attendee list?\n")
    if clear.strip().lower() == "yes":
      double_check = input("Are you absolutely sure? This action cannot be undone.\n")
      if double_check.strip().lower() == "yes":
        people.clear()
        clearScreen()
    else:
      continue

  elif choice == "x":
    clearScreen()
    print("Goodbye.")
    time.sleep(2)
    clearScreen()
    break
  
  