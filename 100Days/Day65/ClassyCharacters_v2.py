import os, random

# screen-clearing function
def clearScreen():
  os.system("cls" if os.name == "nt" else "clear") ## clear screen on Windows ("nt") with "cls" or Linux/MacOS with "clear"

# subroutine for random stat generation
def statGenerator():
  die1 = random.randint(15, 30)
  die2 = random.randint(15, 30)
  stats = die1 + die2
  return stats

# create base class
class character:
  # define shareable class attributes
  health = statGenerator()
  magic = statGenerator()
  
  def __init__(self, name): ## initialize attributes
    self.name = name

# create character subclass
class player(character):
  def __init__(self): ## no additional parameters needed because they're defined below
    self.name = input("Name your player:\n")
    self.nickname = f"{self.name} the Ruthless"
    self.lives = 3
  
  # create a method to determine whether instances of player are living
  def living(self):
    if self.lives >= 0:
      print(f"\n\033[31m{self.nickname}\033[0m lives to fight another day!\n")
    else:
      print(f"\n\033[31m{self.nickname}\033[0m has left the mortal plane.\n")

  # define a print method
  def create(self):
    print(f"\033[36mName\033[0m: {self.name}\t\033[36mNickname\033[0m: {self.nickname}\t\033[36mHealth\033[0m: {self.health}\t\033[36mMagic\033[0m: {self.magic}\t\033[36mLives\033[0m: {self.lives}")

# create a character subclass as a template for further subclasses
class enemy(character):
  # define shareable class attributes
  health = round(statGenerator() * 1.25)
  magic = round(statGenerator() * 1.25)
  type = None
  strength = round(statGenerator() * 1.25)
  
  def __init__(self, name, type): # must pass through arguments for these parameters upon instantiation because they should remain unique for each instance of the class
    self.name = name
    self.type = type
    
# create an enemy subclass
class orc(enemy):
  def __init__(self, name): # must give each instantiation a unique name
    self.name = name
    self.type = "Orc"
    self.speed = round(statGenerator() * 1.25)
  
  # define a print method
  def create(self):
    print(f"\033[36mName\033[0m: {self.name}\t\033[36mHealth\033[0m: {self.health}\t\033[36mMagic\033[0m: {self.magic}\t\033[36mType\033[0m: {self.type}\t\033[36mStrength\033[0m: {self.strength}\t\033[36mSpeed\033[0m: {self.speed}")

# create an enemy subclass
class vampire(enemy):
  def __init__(self, name, day): ## must give each instantiation a name and day/night attribute
    self.name = name
    self.type = "Vampire"
    self.day = day

  # define a print method
  def create(self):
    print(f"\033[36mName\033[0m: {self.name}\t\033[36mHealth\033[0m: {self.health}\t\033[36mMagic\033[0m: {self.magic}\t\033[36mType\033[0m: {self.type}\t\033[36mStrength\033[0m: {self.strength}\t\033[36mDay/Night\033[0m: {'Day' if self.day == True else 'Night'}") 

# instantiate the characters
Player1 = player()
Shuttershock = orc("Shuttershock")
Plasmadrid = orc("Plasmadrid")
Nightpain = vampire("Nightpain", False)
Hemogoblin = vampire("Hemogoblin", True)
Bloodwashen = vampire("Bloodwashen", False)

# create the proper amount of instances in accordance with the challenge
clearScreen()
print("\033[31mYet Another Fantasy Game\033[0m\n")
Player1.create()
Player1.living()
Shuttershock.create()
Plasmadrid.create()
Nightpain.create()
Hemogoblin.create()
Bloodwashen.create()