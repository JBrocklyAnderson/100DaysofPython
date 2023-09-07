import os

def clearScreen():
  os.system("cls" if os.name == "nt" else "clear")

def printToDo():
  clearScreen()
  print("\033[34mTo Do List\033[0m")
  print()
  for item in range(len(toDoList)):
    print(f"\033[34m{item}\033[0m: {toDoList[item]}")
    
toDoList = []

printToDo()

while True:
  printToDo()
  menu = input("""\033[34mView\033[0m List? (v)
\033[32mAdd\033[0m Item? (a)
\033[33mEdit\033[0m Item? (e)
\033[31mRemove\033[0m Item? (r)
\033[31mClear\033[0m Item? (c)
\033[34mExit\033[0m List? (x)\n""").lower()
  
  # adding to the list
  if menu == "a":
    item = input("What would you like to \033[32madd\033[0m?\n")
    # preventing duplicates
    if item not in toDoList:
      toDoList.append(item)
      clearScreen()
    else:
      print("This \033[34mitem\033[0m already exists.")
      input("Press \033[33mENTER\033[0m to continue...")
  
  # removing from the list
  elif menu == "r":
    item = input("What would you like to \033[31mremove\033[0m?\n")
    if item in toDoList:
      # authenticating confirmation
      confirm = input(f"Are you sure you want to \033[31mremove\033[0m {item}?\n").lower()
      if confirm == "yes":
        toDoList.remove(item)
    else:
      print(f"'{item}' was not in the \033[34mlist\033[0m.")
      input("Press \033[33mENTER\033[0m to continue...")
      clearScreen() 

  elif menu == "c":
    clear = input("Are you sure you want to \033[31mclear\033[0m the \033[34mlist\033[0m?\n").lower()
    if clear == "yes":
      print("Are you \033[31mabsolutely\033[0m sure? This \033[31mcannot\033[0m be undone.")
      double_check = input("")
      if double_check == "yes":
        print("Don't say I didn't \033[31mwarn\033[0m you...")
        toDoList.clear()
    else: 
      continue

  # editing the list
  elif menu == "e":
    edit = input("Which \033[34mitem\033[0m would you like to \033[33medit\033[0m?\n")
    if edit in toDoList:
      new_item = input(f"What should {item} be changed to?\n")
      # preventing duplicates
      if new_item not in toDoList:
        index = toDoList.index(edit)
        toDoList[index] = new_item
        clearScreen()
      else:
        print("This \033[34mitem\033[0m already exists.")
        input("Press \033[33mENTER\033[0m to continue...")
    else:
      print(f"'{edit} was not in the list.")
      input("Press \033[33mENTER\033[0m to continue...")
  
  # viewing the menu
  elif menu == "v":
    clearScreen()
    printToDo()
    input("Press \033[33mENTER\033[0m to continue...")
    clearScreen()
  elif menu == "x":
    break