import os

predaDEX = {}

def clearScreen():
  os.system("cls" if os.name == "nt" else "clear")

def printPredaDEX():
  for key, value in predaDEX.items():
    details = []
    details.append(f"\033[31mPredator\033[0m: {key}")
    for subKey, subValue in value.items():
      details.append(f"{subKey}: {subValue}")
    print(" | ".join(details))


while True:
  clearScreen()
  
  # print title
  print("\033[31mWelcome\033[0m to the \033[31mPredaDEX\033[0m\n")

  # get user input
  new = input("Add another \033[31mpredator\033[0m?\n\n").strip().lower()
  
  # get confirmation
  if new in ["y", "yes", "yeah", "ok", "yep", "yup", "okay", "sure", "why not", "go ahead", "definitely", "absolutely", "of course", "sounds good"]:
    predator = input("\nWhat's the name of your \033[31mpredator\033[0m?\n\n")
    type = input("\nWhat kind of \033[31mpredator\033[0m is it?\n\n")
    health = input("\nInitial \033[32mHP\033[0m:  ")
    magic = input("\nInitial \033[36mMagic Points\033[0m:  ")

    # ammend user inputs into dictionary
    print()
    predaDEX[predator] = {"\033[33mType\033[0m": type, "\033[32mHP\033[0m": health, "\033[36mMagic\033[0m": magic}
    printPredaDEX()
    input("\n\nPress ENTER to continue...")
  elif new in ["no", "nah", "no thanks", "nope", "no way", "not a chance"]:
    break
  else:
    clearScreen()
    print("\033[31mInvalid\033[0m response.\n\n")
    input("Press \033[31mENTER\033[0m to continue...")
    



    