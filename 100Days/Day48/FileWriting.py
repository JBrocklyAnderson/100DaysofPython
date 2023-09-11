# open the file with `ammend +`; this will add to the file every time the program is executed to completion
f = open("high.score", "a+")

import os

def clearScreen():
  os.system("cls" if os.name == "nt" else "clear")

# input loop
while True:
  print("HIGH SCORES!\n")
  
  highScores = {
    "initials": input("Input user initials: "),
    "score": int(input("Input user score: "))
  }
  print("\nAdded user to high scores.\n")
 
  # write changes to the file
  f.write(f"{highScores}\n\n")

  if input("Add another? ").strip().lower() == "yes":
    clearScreen()
    continue
  
  # complete the program
  else:
    break

# save/close the file
f.close()