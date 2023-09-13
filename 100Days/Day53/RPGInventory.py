# import libraries
import os, time

# initialize a list to carry inventory items
inventory = []

# autoload invetory.rpg contents
try:
  f = open("inventory.rpg", "r")
  inventory = eval(f.read())
  f.close()
except Exception as errorType:
  print("ERROR: Unable to access inventory.\n")
  print(f"{errorType}\n")

# screen-clearing function
def clearScreen():
  os.system("cls" if os.name == "nt" else "clear")

# method for adding items
def addItem():
  clearScreen()
  ## ask what the user would like to add
  item = input("What's the item?\n\n").strip().title()
  try:
    ## ask how many of the item the user would like to add
    quantity = int(input(f"Quantity of '{item}(s)' to add:  "))
    ## for the given quantity
    for i in range(quantity):
      ## add the item(s)
      inventory.append(item)
    print(f"{quantity} {item}(s) have been added to your inventory.")
  ## handle invalid user input
  except:
    print("Please enter a valid number.")
  input("\n↲ Enter to continue...")

# method for viewing the inventory
def viewItems():
  clearScreen()
  ## what would the user like to view
  view = input("View all (a)?\nView specific (s)?\n\n").strip().lower()
  if view == "a":
    clearScreen()
    #3 if items exist in the inventory
    if inventory:
      ## print each unique item and how many there are 
      unique = set(inventory)
      for item in unique:
        print(f"{item}: {inventory.count(item)}")
    else:
      print("You have nothing in your inventory.")
  elif view == "s":
    clearScreen()
    item = input("Which item?\n\n").strip().title()
    count = inventory.count(item)
    if count:
      clearScreen()
      print(f"You have {count} {item}(s).")
    else:
      clearScreen()
      print(f"You do not have any {item}(s).")
  input("\n↲ Enter to continue...")

# method for removing items
def removeItem():
  clearScreen()
  ## ask what the user would like to remove
  removeWhich = input("Which item would you like to remove?\n\n").strip().title()
  ## check if item exists in the inventory
  if removeWhich not in inventory:
    print(f"You don't have any {removeWhich}(s) in your inventory.")
    input("\n↲ Enter to continue...")
    return 
    
  else:
    try:  
      ## ask how many of the item the user wants to remove
      quantity = int(input(f"\nQuantity of '{removeWhich}(s)' to remove:  "))
      ## check if the inventory contains the specified quantity 
      if quantity > inventory.count(removeWhich):
        print(f"Can't remove {quantity} {removeWhich}(s). You only have {inventory.count(removeWhich)} {removeWhich}(s) in your inventory.")
        input("\n↲ Enter to continue...")
        return
      ## ask for confirmation to remove
      confirm = input(f"\nAre you sure you want to remove {quantity} {removeWhich}(s) from your inventory?\n\n").strip().lower()
      if confirm in ["y", "yes"]:
        ## for every instance
        for i in range(quantity):
          ## remove the item
          inventory.remove(removeWhich)
        print(f"\n{quantity} {removeWhich}(s) were removed from your inventory.")
      else:
        print(f"{quantity} {removeWhich}(s) will remain in your inventory.")
    ## handle invalid user input
    except:
      print("Please enter a valid number.")
  input("\n↲ Enter to continue...")

while True:
  clearScreen()
  menu = input("Add (a)\nView (v)\nRemove (r)\nExit (x)\n\n")
  if menu == 'a':
    addItem()
  elif menu == 'v':
    viewItems()
  elif menu == 'r':
    removeItem()
  elif menu == 'x':
    break
  else:
    print("Invalid choice.")
    input("\n↲ Enter to continue...")

  # autosave inputs to file
  f = open("inventory.rpg", "w") # enable `write` permissions to prevent inaccurate duplication
  f.write(str(inventory))
  f.close()
    