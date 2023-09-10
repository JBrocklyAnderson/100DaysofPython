
# import necessary libraries
import os

# define a subroutine that keeps the console clean
def clearScreen():
  os.system("cls" if os.name == "nt" else "clear")

# store color values in a dictionary
colorCoder = {
  "reset": "\033[0m",
  "red": "\033[31m",
  "green": "\033[32m",
  "blue": "\033[34m",
  "yellow": "\033[33m",
  "cyan": "\033[36m",
}

# create a predator for the PredaDEX
predaDEX = {
  "name": None,
  "type": None,
  "special": None,
  "health": None,
  "strength": None
}

# have user fill in the PredaDEX 
predaDEX["name"] = input("Name your predator:  ").strip().title()
print()
predaDEX["type"] = input("What type of predator is it? (Fire / Air / Water / Earth / Spacetime)  ").strip().lower()
print()
predaDEX["special"] = input("What's its special move?  ").strip().lower()
print()
predaDEX["health"] = input("Initial HP:  ").strip()
print()
predaDEX["strength"] = input("Initial Strength:  ").strip()

# print the PredaDEX
for key, value in predaDEX.items():
  clearScreen()
  # color the text according to predator type
  if predaDEX["type"] == "fire":
    print(f"{colorCoder['red']} Our PredaDEX indicates that your predator is called {predaDEX['name']}. It is a {predaDEX['type']}-type predator with the ability to {predaDEX['special']}.{colorCoder['reset']}")
  elif predaDEX["type"] == "earth":
    print(f"{colorCoder['green']} Our PredaDEX indicates that your predator is called {predaDEX['name']}. It is an {predaDEX['type']}-type predator with the ability to {predaDEX['special']}.{colorCoder['reset']}")
  elif predaDEX["type"] == "water":
    print(f"{colorCoder['blue']} Our PredaDEX indicates that your predator is called {predaDEX['name']}. It is a {predaDEX['type']}-type predator with the ability to {predaDEX['special']}.{colorCoder['reset']}")
  elif predaDEX["type"] == "air":
    print(f"{colorCoder['yellow']} Our PredaDEX indicates that your predator is called {predaDEX['name']}. It is an {predaDEX['type']}-type predator with the ability to {predaDEX['special']}.{colorCoder['reset']}")
  elif predaDEX["type"] == "spacetime":
    print(f"{colorCoder['cyan']} Our PredaDEX indicates that your predator is called {predaDEX['name']}. It is a {predaDEX['type']}-type predator with the ability to {predaDEX['special']}.{colorCoder['reset']}")