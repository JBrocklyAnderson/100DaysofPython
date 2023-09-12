import random, os, time

ideaBank = []

def clearScreen():
  os.system("cls" if os.name == "nt" else "clear")

def loadIdeas():
  f = open("my.ideas", "r")
  
  # append each line in the file to the idea bank
  for line in f:
    ideaBank.append(line.strip())

def menuPrint():
  print("💡 Brilluminance Notepad 📗\n")
  print("Illuminating the world, one idea at a time!\n")

def addIdea():
  clearScreen()
  idea = input("What's your brilliant idea?\n\n").strip().capitalize()

    # preventing blank ideas
  while not idea:
    print("You can't add a blank idea!")
    idea = input("Please enter a valid idea:\n\n").strip().capitalize()
      
  # add idea to the bank
  ideaBank.append(idea)

  # save idea to the file
  f = open("my.ideas", "a")
  f.write(f"{idea}\n")
  f.close()
  
  print(f"\n'{idea}' added to the notepad.")
  time.sleep(2)
  clearScreen()

def randomIdea():
  clearScreen()
  if ideaBank:
    pullIdea = random.choice(ideaBank)
    print(f"{pullIdea}")
    input("\n↲ Enter to continue...")
    clearScreen()
  else:
    elseAdd = input("No ideas yet. Add one (Y/N) ?\n\n").strip().lower()
    if elseAdd in ["y", "yes"]:
      addIdea()
    else:
      input("↲ Enter to continue...")

# loading the file function
loadIdeas()

while True:
  menuPrint()
  menu = input("""Add idea (a)?
Random idea? (r)
Leave notepad? (x)\n\n""")

  if menu == "a":
    addIdea()
  elif menu == "r":
    randomIdea()
  elif menu == "x":
    break
  else:
    clearScreen()
    