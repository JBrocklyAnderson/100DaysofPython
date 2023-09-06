import os

print("🗓️  \033[32mTo \033[34mDo \033[31mList\033[0m 🗓️")
print()

toDoList = []

# ensure clearScreen is compatible across systems
def clearScreen():
  os.system("cls" if os.name == "nt" else "clear")

# define how the list will print
def printToDo():
  print("\033[32mTo \033[34mDo \033[31mList\033[0m")
  print()
  for item in toDoList:
    print(f"\033[32m{item}\033[0m")
  print()

# create menu options
while True:
  menu = input("""\033[32mAdd\033[0m Item? (a)
\033[31mRemove\033[0m Item? (r)
\033[34mView\033[0m List? (v)
\033[34mExit\033[0m List?\(e)\n""").lower()
  if menu == "a":
    item = input("What's next on the agenda?:\n")
    toDoList.append(item)
    clearScreen()
  elif menu == "r":
    item = input("What would you like to remove?: ")
    if item in toDoList:
      toDoList.remove(item)
      clearScreen()
    else:
      print(f"'{item}' was not in the list.")
      input("Press ENTER to continue...")
      clearScreen()
  elif menu == "v":
    clearScreen()
    printToDo()
    input("Press ENTER to continue...")
    clearScreen()
  elif menu == "e":
    break
  