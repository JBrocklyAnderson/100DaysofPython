# import necessary libraries
import os, time, random

# initialize an empty list
toDoList = []

fileExists = True
try:
  # parse the contents of the file
  f = open("toDoList.txt", "r")
  toDoList = eval(f.read())
  f.close()
except:
  fileExists = False

# define screen-clearing function
def clearScreen():
  os.system("cls" if os.name == "nt" else "clear")

# define printing method
def printToDo():
  clearScreen()
  print("\033[32;40mTo-Do List\033[0m\n")
  for item in toDoList:
    task, due, priority = item
    print(f"\033[34mTask\033[0m: \033[32m{task}\033[0m | \033[34mDue By\033[0m: \033[32m{due}\033[0m | \033[34mPriority\033[0m: \033[32m{priority}\033[0m")

# create a way to view the list
def viewList():
  clearScreen()
  choice = input("\033[34mView\033[0m All (a) or \033[34mView\033[0m by \033[33mPriority\033[0m (p)?\n\n").strip().lower() # what does the user want to see
  if choice == "a":
    printToDo()
  elif choice == "p":
    clearScreen()
    priority = input("Enter priority (\033[31mhigh\033[0m / \033[35mmedium\033[0m / \033[33mlow\033[0m):\n\n").strip().lower()
    print(f"\n\033[34mTo Do List\033[0m with {priority.upper()} priority\n")
    for item in toDoList:
      task, due, p = item
      if p == priority.lower():
        print(f"\033[34mTask\033[0m: \033[32m{task}\033[0m | \033[34mDue By\033[0m: \033[32m{due}\033[0m | \033[34mPriority\033[0m: \033[32m{priority}\033[0m") 
  else:
    print("\n\033[31mInvalid\033[0m \033[33mpriority\033[0m!")
  input("\nPress \033[32mENTER\033[0m to \033[34mcontinue\033[0m...")

# create a way to add items
def addItem():
  clearScreen()
  task = input("What to \033[34mdo\033[0m?\n\n").strip().capitalize()
  print()
  due = input("When is it \033[33mdue\033[0m?\n\n").strip().capitalize()
  print()
  priority = input("How important is it (\033[31mhigh\033[0m / \033[35mmedium\033[0m / \033[33mlow\033[0m)?\n\n").strip().capitalize()
  if any(item[0] == task.lower() for item in toDoList) or priority.lower() not in ["high", "medium", "low"]:
    print(f"Either '{task}' already exists in your \033[34mlist\033[0m or you've entered an \033[31minvalid\033[0m \033[33mpriority\033[0m.")
    time.sleep(2)
  else:
    toDoList.append([task, due, priority])

# create a way to edit items
def editItem():
  clearScreen()
  editTask = input("Which \033[34mtask\033[0m would you like to \033[33medit\033[0m?\n\n").strip().lower()
  for index, item in enumerate(toDoList):
    if item[0].strip().lower() == editTask: # make sure user choice matches task in list
      newTask = input("\nNew \033[34mTask\033[0m:\n\n").strip().capitalize()
      newDue = input("\nNew \033[33mDue\033[0m Date:\n\n").strip().capitalize()
      newPriority = input("\nNew \033[32mPriority\033[0m (\033[31mhigh\033[0m / \033[35mmedium\033[0m / \033[33mlow\033[0m):\n\n").strip().capitalize()
      if newPriority.lower() in ["high", "medium", "low"]: # validate priority
        toDoList[index] = [newTask, newDue, newPriority] # replace toDoList[index]
        clearScreen()
        print("\033[34mTask\033[0m \033[32msuccessfully\033[0m \033[33mupdated\033[0m!")
        break
      else:
        print("\n\033[31mInvalid\033[0m \033[33mpriority\033[0m!")
  else:
    print(f"'\033[34m{editTask}\033[0m' \033[31mnot\033[0m found in \033[34mlist\033[0m.\n")
  input("\nPress \033[32mENTER\033[0m to \033[34mcontinue\033[0m...")

# create a way to remove items
def removeItem():
  clearScreen()
  removeTask = input("Which \033[34mtask\033[0m would you like to \033[31mremove\033[0m?\n\n").strip().capitalize()
  foundItem = False
  for item in toDoList:
    if item[0] == removeTask:
      confirm = input(f"\nAre you sure you want to remove '{removeTask}'?\n\n")
      if confirm in ["yes", "y"]:
        toDoList.remove(item)
        print("\n\033[34mTask\033[0m \033[32msuccessfully\033[0m \033[31mremoved\033[0m!")
        foundItem = True
        break
  if not foundItem:
    print(f"'\033[34m{removeTask}\033[0m' \033[31mnot\033[0m found in \033[34mlist\033[0m.\n")
  input("\nPress \033[32mENTER\033[0m to \033[34mcontinue\033[0m...")  

# create a way to clear list
def clearList():
  clearScreen()
  clear = input("Are you sure you want to \033[31mclear\033[0m the \033[34mlist\033[0m?\n").strip().lower()
  if clear in ["yes", "y"]:
    print("Are you \033[31mabsolutely\033[0m sure? This \033[31mcannot\033[0m be undone.\n")
    double_check = input("").strip().lower()
    if double_check in ["yes", "y"]:
      print("Don't say I didn't \033[31mwarn\033[0m you...")
      time.sleep(2)
      toDoList.clear()

while True:
  clearScreen()
  print("\033[32;40mTo-Do List\033[0m\n")
  menu = input("""\033[34mView\033[0m List? (v)
\033[32mAdd\033[0m Item? (a)
\033[33mEdit\033[0m Item? (e)
\033[31mRemove\033[0m Item? (r)
\033[31mClear\033[0m List? (c)
\033[34mExit\033[0m List? (x)\n\n""").strip().lower()

  view = ["v", "view"]
  add = ["a", "add"]
  edit = ["e", "edit"]
  remove = ["r", "remove"]
  clear = ["c", "clear"]
  exit = ["x", "exit"]
  
  # adding to the list
  if menu in view:
    viewList()
  elif menu in add:
    addItem()
  elif menu in edit:
    editItem()
  elif menu in remove:
    removeItem()
  elif menu in clear:
    clearList()
  elif menu in exit:
    break
  else:
    print("\033[31mInvalid\033[0m choice.")
    time.sleep(1)

  if fileExists:
    try:
      os.mkdir("Backup-Files")
    except:
      pass
    randomFileName = f"toDoListBackup{random.randint(1,100000000)}.txt"
    # open the shell and command it to create a copy `f"'copy' FileToBeCopied placeToCopyInto/nameOfCopy.txt"
    os.popen(f"cp toDoList.txt Backup-Files/{randomFileName}")
  
  # save user inputs into file
  f = open("toDoList.txt", "w")
  f.write(str(toDoList))
  f.close()