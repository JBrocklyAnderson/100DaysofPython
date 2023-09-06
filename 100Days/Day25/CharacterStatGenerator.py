import random

print("🪄 CHARACTER STAT GENERATOR 🪄")
print()
print("We are going to generate character stats across six domains by multiplying the outputs of two rolled dice, but first..., but first...")
print()

# creating a subroutine that multiplies two rolled die to generate a stat value
def stat_generator():
  die1 = round(random.randint(1, 10) * 1.25)
  die2 = round(random.randint(1, 10) * 1.25)
  stats = die1 + die2
  return stats

# defining affirmatives answers for the user to provide to build new characters with new stats
affirmatives = ["yes", "yeah", "sure", "why not", "i guess", "sounds good", "sounds great", "sounds groovy", "dope", "hell yeah", "ok", "okay", "for sure", "definitely", "absolutely", "you got it", "tight", "sick", "fire"]

# setting the initial response so that the loop begins properly
new_character = "yes"

# making sure the loop reinitializes with an affirmative answer
while new_character in affirmatives:
  print()
  name = input("Give your character a name: ")
  print()
  
  # generating points for each stat domain 
  strength = stat_generator()
  dexterity = stat_generator()
  constitution = stat_generator()
  intelligence = stat_generator()
  wisdom = stat_generator()
  charisma = stat_generator()

  print(f"{name} has the following character stats:")
  print()
  print(f"Strength: {strength}")
  print(f"Dexterity: {dexterity}")
  print(f"Constitution: {constitution}")
  print(f"Intelligence: {intelligence}")
  print(f"Wisdom: {wisdom}")
  print(f"Charisma: {charisma}")
  print()

  # allowing the user to reloop or exit
  new_character = input("Do you want to create a new character? ")