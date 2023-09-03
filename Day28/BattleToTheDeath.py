import random, os, time

# introducing an opening screen
print("The World of Tomorrow")
time.sleep(1)
os.system("clear")

print("💀 BATTLE EDITION 💀")
time.sleep(1)
os.system("clear")

# rolling dice to generate health
def health_stat():
  die1 = round(random.randint(1, 6))
  die2 = round(random.randint(1, 12))
  health = ((die1 * die2) / 2) + 10
  return health

# rolling dice to generate strength
def strength_stat():
  die1 = round(random.randint(1, 6))
  die2 = round(random.randint(1, 8))
  strength = ((die1 * die2) / 2) + 12
  return strength

# generating two characters
def character1():
  char_name = input("Player 1, name your fighter:\n")
  print()
  char_type = input("Who are they? (Neuro-Hacker, Super Soldier, Mech-Pilot, Psionic Operative, Eco-Saboteur):\n")
  print()
  return char_name, char_type, health_stat(), strength_stat()

def character2():
  char_name = input("Player 2, name your fighter:\n")
  print()
  char_type = input("Who are they? (Neuro-Hacker, Super Soldier, Mech-Pilot, Psionic Operative, Eco-Saboteur):\n")
  print()
  return char_name, char_type, health_stat(), strength_stat()

# setting the parameters of battle
def battle(char1, char2):
  round_number = 1
  while char1[2] > 0 and char2[2] > 0:
    os.system("clear")
    print("💀 THE BATTLE BEGINS 💀")
    roll1, roll2 = random.randint(1, 6), random.randint(1, 6)
    if roll1 > roll2:
      damage = abs(char1[3] - char2[3])
      char2[2] -= damage
      print(f"{char1[0]} wins round {round_number}!")
      print(f"{char2[0]} takes {damage} damage.")
    elif roll2 > roll1:
      damage = abs(char2[3] - char1[3])
      char1[2] -= damage
      print(f"{char2[0]} wins round {round_number}!")
      print(f"{char1[0]} takes {damage} damage.")
    else:
      print("It's a draw!")
    

    print()
    print(f"{char1[0]} still has {char1[2]} health.")
    print(f"{char2[0]} still has {char2[2]} health.")
  
    if char1[2] <= 0:
      print()
      print(f"Oh no! {char1[0]} has been brutally slain in battle.")
      print()
      print(f"{char2[0]} defeated {char1[0]} in {round_number} rounds!")
      break

    if char2[2] <= 0:
      print()
      print(f"Oh no! {char2[0]} has been brutally slain in battle.")
      print()
      print(f"{char1[0]} defeated {char2[0]} in {round_number} rounds!")
      break
  
    round_number += 1
    input("Press enter for next round!")

# obvious and secret affirmations
affirmatives = ["yes", "yeah", "sure", "why not", "i guess", "sounds good", "sounds great", "sounds groovy", "of course", "hell yeah", "ok", "okay", "for sure", "definitely", "absolutely", "assuredly", "obviously"]

# creating the main menu
while True:
  # clearing the main menu
  os.system("clear")
  print("💀 BATTLE TIME 💀")
  print()
  char1 = character1()
  char2 = character2()

  winner = battle(list(char1), list(char2))
  if winner == char1[0]:
    loser = char2[0]
  else:
    loser = char1[0]

  # pausing the reinitialization prompt
  time.sleep(2)
  print()
  new_game = input(f"{loser} may have lost the battle, but will they win the war?\n").lower()
  if new_game not in affirmatives:
    break