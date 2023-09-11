# import libraries
import random, os

# screen-clearing function
def clearScreen():
  os.system("cls" if os.name == "nt" else "clear")

# define preset characters in 2D dictionary
anime = {"Naruto" :{"Strength": 9, "Intelligence": 6, "Determination": 10, "Teamwork": 9}, 
         "Sasuke": {"Strength": 9, "Intelligence": 8, "Determination": 9, "Teamwork": 6},
         "Gaara": {"Strength": 8, "Intelligence": 7, "Determination": 8, "Teamwork": 7},
         "Kakashi": {"Strength": 8, "Intelligence": 9, "Determination": 8, "Teamwork": 9},
         "Itachi": {"Strength": 9, "Intelligence": 10, "Determination": 10, "Teamwork": 7}}

# function to print a character list
def printChar(wait = True): 
  clearScreen()
  print("Character Cards\n")

  # print every key (character's name)
  for key in anime.keys(): 
    print(key)
  if wait: # user is required to press enter
    input("\n↲ Enter to return to main menu.")

# function to print list of stats
def printStat():
  clearScreen()
  print("Character Stats\n")
  
  # print every subkey in key "Naruto" since all keys have the same subkeys
  for stat in anime["Naruto"].keys():
    print(stat)
  input("\n↲ Enter to return to main menu.")

# set affirmative answers for if-statements
affirm = ["y", "yes", "yea", "yeah", "yeehaw", "ok", "yep", "yup", "okay", "sure", "why not", "go ahead", "definitely", "absolutely", "of course", "sounds good"]

# function to add characters
def addChar():
  clearScreen()
  printChar(wait = False) # ignore input requirement
  if input("\nWould you like to add a character?\n\n").strip().lower() in affirm:
    newChar = input("\nName: ").strip().capitalize()
    if newChar in anime:
      print()
      print(f"{newChar} is already in the list.")
    else:
      # appending the new character to the 2D dictionary
      anime[newChar] = {
        "Strength": int(input("Strength: ")),
        "Intelligence": int(input("Intelligence: ")),
        "Determination": int(input("Determination: ")),
        "Teamwork": int(input("Teamwork: "))
      }
      clearScreen()
      printChar(wait = False) # ignore input requirement
      print(f"\n{newChar} added successfully!") 
    input("\n↲ Enter to return to main menu.")

# function to edit characters
def editChar():
  clearScreen()
  if input("Would you like to edit a character?\n\n").strip().lower() in affirm:
    printChar(wait = False) # ignore input requirement
    editWhich = input("Which character?\n\n").strip().capitalize()
    if editWhich in anime:
      print()
      
      # reset subkey subvalues
      anime[editWhich] = {
                "Strength": int(input("Strength: ")),
                "Intelligence": int(input("Intelligence: ")),
                "Determination": int(input("Determination: ")),
                "Teamwork": int(input("Teamwork: "))
            }    
    else:
      print(f"{editWhich} does not appear to be in the list.")
    input("\n↲ Enter to return to main menu.")

# function to remove characters
def removeChar():
  clearScreen()
  if input("Would you like to remove a character?\n\n").strip().lower() in affirm:
    printChar(wait = False) # ignore input requirement
    removeWhich = input("\nWhich character?\n\n").strip().capitalize()
    if removeWhich in anime:
      
      # ask for confirmation
      confirm = input(f"\nAre you sure you want to remove {removeWhich}?\n\n")
      if confirm in affirm:
        del anime[removeWhich] # remove 
        clearScreen()
        printChar(wait = False)
        print(f"\n{removeWhich} successfully removed.")
      
    else:
      print(f"\n'{removeWhich}' does not appear in the list.")
    input("\n↲ Enter to return to main menu.")

# set up point system
points = 0
compPoints = 0

# function to reset the points
def reset():
  global points
  global compPoints
  points = 0
  compPoints = 0

# function to initiate the game
def chooseChar():
  global points
  global compPoints

  while True:
    reset()
    clearScreen()
    printChar(wait = False) # ignore input requirement
    choiceChar = input("\nChoose your character:  \n\n").strip().capitalize()
    if choiceChar in anime:
      print("""
      Available stats:
      Strength
      Intelligence
      Determination
      Teamwork\n""")
      choiceStat = input(f"Which stat will {choiceChar} use?\n\n").strip().capitalize()
      
      if choiceStat in anime[choiceChar]:
        
        # generate random oponent
        genCharName = random.choice(list(anime.keys()))
        genChar = anime[genCharName]
  
        # player 1 wins
        if anime[choiceChar][choiceStat] > genChar[choiceStat]:
          clearScreen()
          points += 1
          print(f"\n{choiceChar} won {choiceStat}: {anime[choiceChar][choiceStat]} to {genChar[choiceStat]} against {genCharName}!")
  
        # player 1 and computer tie
        elif anime[choiceChar][choiceStat] == genChar[choiceStat]:
          clearScreen()
          print(f"\n{choiceChar} tied {genCharName}: {anime[choiceChar][choiceStat]} to {genChar[choiceStat]}")
  
        #computer wins
        else:
          clearScreen()
          compPoints += 1
          print(f"\n{genCharName} won {choiceStat}: {genChar[choiceStat]} to {anime[choiceChar][choiceStat]} against {choiceChar}")
        print(f"\nYou: {points} of 5\nComputer: {compPoints} of 5")
        if points == 3:
          print("\nYou win!\n")
        elif compPoints == 3:
          print("\nComputer wins!\n)")
          
        if input("Play again?\n\n").strip().lower() not in affirm:
          break
      else:
        print("\nInvalid stat choice.")
    else:
      print("\nInvalid character choice.")
    input("\n↲ Enter to return to main menu.")

  
  
# start loop
while True:
  clearScreen()
  print("Welcome to the Card Game")
  menu = input(
  """
  Stat overview: (s)
  View characters (v):
  Add character (a):
  Edit character (e):
  Remove character (r):
  Play game (p):
  Exit game (x):\n
  """).strip().lower()
  
  if menu == "s":
    printStat()
  elif menu == "v":
    printChar()
  elif menu == "a":
    clearScreen()
    addChar()
  elif menu == "e":
    editChar()
  elif menu == "r":
    removeChar()
  elif menu == "p":
    chooseChar()
  elif menu == "x":
    break
  else:
    print(f"'{menu}' is not a valid option.")
    input("Press enter to try again.")
    
    
  