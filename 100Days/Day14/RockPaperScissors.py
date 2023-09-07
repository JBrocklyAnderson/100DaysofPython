print("Let's play (r) Rock, (p) Paper, (s) Scissors!")
print()
print("Your moves will not appear on the screen. This way, the game can be still be fun!")
print()
name1 = input("Player 1, what's your name? ")
name2 = input("Player 2, what's your name? ")
from getpass import getpass as input
player1 = input(name1 + ", what's your move? ")
player2 = input(name2 + ", what's your move? ")
print()
if player1 == "r" and player2 == "s":
  print(name1, "crushs", name2, "'s rusty scissors with a mighty rock!")
elif player1 == "p" and player2 == "r":
  print(name1, "snuffs the sunlight out of", name2, "'s puny rock with a gargantuan piece of paper!")
elif player1 == "s" and player2 == "p":
  print(name1, "uses a pair of deadly scissors to hack away at", name2, "'s flimsy paper!")
elif player2 == "r" and player1 == "s":
  print(name2, "crushs", name1, "'s rusty scissors with a mighty rock!")
elif player2 == "p" and player1 == "r":
  print(name2, "snuffs the sunlight out of", name1, "'s puny rock with a gargantuan piece of paper!")
elif player2 == "s" and player1 == "p":
  print(name2, "uses a pair of deadly scissors to hack away at", name1, "'s flimsy paper!")
elif player1 == "r" and player2 == "r":
  print("Two rocks came crashing together in a thunderous show of fireworks, but both rolled away unscathed.")
elif player1 == "p" and player2 == "p":
  print("On the battlefield, a ninja-like strip of paper sliced right past another, equally agile. No blood came forth.")
else:
  print("Try as they might, the two pairs of scissors couldn't get an edge on each other.")