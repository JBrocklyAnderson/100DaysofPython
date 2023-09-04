# For the future, add several different winning messages for each way a player can win, then randomize when their outputted for the players.

print("Let's play Spacetime! This two-player game is kind of like Rock, Paper, Scissors, but there's five different battle moves we can make each round. These moves are based on the ancient elements: spacetime (s), air (a), water (w), earth (e), and fire (f). These relationships are for pure enjoyment; they should not be taken for scientific truth.")
print()
print("Don't worry, each player's moves will not appear on the screen as they type. This way, the game can still be fair, fun, and unpredictable!")
print()
wins1 = 0 # setting player1's initial score 
wins2 = 0 # setting player2's initial score
winning_moves = ["s", "f", "e", "w", "a"] 
valid_responses = ["yes", "sure", "why not", "ok", "okay", "definitely", "absolutely", "yeah", "yep", "yup", "yea", "yee" "yeppers", "yeehaw", "obviously"] # setting valid responses to continue the game

name1 = input("Player 1, what's your name? ")
name2 = input("Player 2, what's your name? ")
print()
from getpass import getpass as hidden_input # hiding player input
while True:
  player1 = hidden_input(name1 + ", what's your move? ")
  player2 = hidden_input(name2 + ", what's your move? ")
  print()
  
## all the ways player1 can win with spacetime
  if player1 == "s" and player2 == "a":
    print(name1, "sucks", name2, "'s wisp of air into the infinite void of spacetime!")
    wins1 += 1
    print()
    print(name1, "'s score:", wins1)
    print(name2, "'s score:", wins2)
    print()
    cont = input("Do you want to continue playing? ").lower()
    if cont not in valid_responses:
      break
      
  elif player1 == "s" and player2 == "w":
    print(name1, "sucks", name2, "'s puddle of water into the infinite void of spacetime!")
    wins1 += 1
    print()
    print(name1, "'s score:", wins1)
    print(name2, "'s score:", wins2)
    print()
    cont = input("Do you want to continue playing? ").lower()
    if cont not in valid_responses:
      break

  
# all the ways player1 can win with air
  elif player1 == "a" and player2 == "w":
    print(name2, "'s puddle of water evaporates into", name1, "'s immense ocean of air!")
    wins1 += 1
    print()
    print(name1, "'s score:", wins1)
    print(name2, "'s score:", wins2)
    print()
    cont = input("Do you want to continue playing? ").lower()
    if cont not in valid_responses:
      break
    elif cont in valid_responses:
      continue
      
  elif player1 == "a" and player2 == "e":
    print(name2, "'s brittle earth disintegrate's into", name1, "'s immense ocean of air!")
    wins1 += 1
    print()
    print(name1, "'s score:", wins1)
    print(name2, "'s score:", wins2)
    print()
    cont = input("Do you want to continue playing? ").lower()
    if cont not in valid_responses:
      break

# all the ways player1 can win with water  
  elif player1 == "w" and player2 == "e":
    print(name1, "'s relentless pounding of water disintegrates", name2, "'s brittle earth!")
    wins1 += 1
    print()
    print(name1, "'s score:", wins1)
    print(name2, "'s score:", wins2)
    print()
    cont = input("Do you want to continue playing? ").lower()
    if cont not in valid_responses:
      break      
      
  elif player1 == "w" and player2 == "f":
    print(name1, "'s relentless pounding of water snuffs out", name2, "'s smoldering fire!")
    wins1 += 1
    print()
    print(name1, "'s score:", wins1)
    print(name2, "'s score:", wins2)
    print()
    cont = input("Do you want to continue playing? ").lower()
    if cont not in valid_responses:
      break

  
# all the ways player1 can win with earth
  elif player1 == "e" and player2 == "f":
    print(name1, "'s suffocating weight of earth smothers", name2, "'s smoldering fire!")
    wins1 += 1
    print()
    print(name1, "'s score:", wins1)
    print(name2, "'s score:", wins2)
    print()
    cont = input("Do you want to continue playing? ").lower()
    if cont not in valid_responses:
      break

  elif player1 == "e" and player2 == "s":
    print(name1, "'s dense ball of earth floats effortlessly through the void of", name2, "'s spacetime!")
    wins1 += 1
    print()
    print(name1, "'s score:", wins1)
    print(name2, "'s score:", wins2)
    print()
    cont = input("Do you want to continue playing? ").lower()
    if cont not in valid_responses:
      break

# all the ways player1 can win with fire
  elif player1 == "f" and player2 == "s":
    print(name1, "'s blazing stellar fire outshines entire galaxies across the bleak darkness of", name2, "'s spacetime!")
    wins1 += 1
    print()
    print(name1, "'s score:", wins1)
    print(name2, "'s score:", wins2)
    print()
    cont = input("Do you want to continue playing? ").lower()
    if cont not in valid_responses:
      break
      
  elif player1 == "f" and player2 == "a":
    print(name1, "'s searing fire swallows", name2, "'s wisp of air!")
    wins1 += 1
    print()
    print(name1, "'s score:", wins1)
    print(name2, "'s score:", wins2)
    print()
    cont = input("Do you want to continue playing? ").lower()
    if cont not in valid_responses:
      break
  
# all the ways player2 can win with spacetime
  elif player2 =="s" and player1 == "a":
    print(name2, "sucks", name1, "'s wisp of air into the infinite void of spacetime!")
    wins2 += 1
    print()
    print(name1, "'s score:", wins1)
    print(name2, "'s score:", wins2)
    print()
    cont = input("Do you want to continue playing? ").lower()
    if cont not in valid_responses:
      break
      
  elif player2 == "s" and player1 == "w":
    print(name2, "sucks", name1, "'s puddle of water into the infinite void of spacetime!")
    wins2 += 1
    print()
    print(name1, "'s score:", wins1)
    print(name2, "'s score:", wins2)
    print()
    cont = input("Do you want to continue playing? ").lower()
    if cont not in valid_responses:
      break

# all the ways player2 can win with air  
  elif player2 == "a" and player1 == "w":
    print(name1, "'s puddle of water evaporates into", name2, "'s immense ocean of air!")
    wins2 += 1
    print()
    print(name1, "'s score:", wins1)
    print(name2, "'s score:", wins2)
    print()
    cont = input("Do you want to continue playing? ").lower()
    if cont not in valid_responses:
      break
      
  elif player2 == "a" and player1 == "e":
    print(name1, "'s brittle earth disintegrate's into", name1, "'s immense ocean of air!")
    wins2 += 1
    print()
    print(name1, "'s score:", wins1)
    print(name2, "'s score:", wins2)
    print()
    cont = input("Do you want to continue playing? ").lower()
    if cont not in valid_responses:
      break    
    
# all the ways player2 can win with water  
  elif player2 == "w" and player1 == "e":
    print(name2, "'s relentless pounding of water disintegrates", name1, "'s brittle earth!")
    wins2 += 1
    print()
    print(name1, "'s score:", wins1)
    print(name2, "'s score:", wins2)
    print()
    cont = input("Do you want to continue playing? ").lower()
    if cont not in valid_responses:
      break
      
  elif player1 == "w" and player2 == "f":
    print(name2, "'s relentless pounding of water snuffs out", name1, "'s smoldering fire!")
    wins2 += 1
    print()
    print(name1, "'s score:", wins1)
    print(name2, "'s score:", wins2)
    print()
    cont = input("Do you want to continue playing? ").lower()
    if cont not in valid_responses:
      break

# all the ways player2 can win with earth
  elif player2 == "e" and player1 == "f":
    print(name2, "'s suffocating weight of earth smothers", name1, "'s smoldering fire!")
    wins2 += 1
    print()
    print(name1, "'s score:", wins1)
    print(name2, "'s score:", wins2)
    print()
    cont = input("Do you want to continue playing? ").lower()
    if cont not in valid_responses:
      break
      
  elif player1 == "e" and player2 == "s":
    print(name1, "'s dense ball of earth floats effortlessly through the void of", name2, "'s spacetime!")
    wins2 += 1
    print()
    print(name1, "'s score:", wins1)
    print(name2, "'s score:", wins2)
    print()
    cont = input("Do you want to continue playing? ").lower()
    if cont not in valid_responses:
      break

# all the ways player2 can win with fire
  elif player2 == "f" and player2 == "s":
    print(name2, "'s blazing stellar fire outshines entire galaxies across the bleak darkness of", name1, "'s spacetime!")
    wins2 += 1
    print()
    print(name1, "'s score:", wins1)
    print(name2, "'s score:", wins2)
    print()
    cont = input("Do you want to continue playing? ").lower()
    if cont not in valid_responses:
      break
      
  elif player2 == "f" and player2 == "a":
    print(name1, "'s blazing fire ignites the oxygen in", name2, "'s puff of air!")
    wins2 += 1
    print()
    print(name1, "'s score:", wins1)
    print(name2, "'s score:", wins2)
    print()
    cont = input("Do you want to continue playing? ").lower()
    if cont not in valid_responses:
      break


# all the ways both players can win
  elif player2 =="s" and player1 == "s":
    print("The collision of two infinite spacetimes produces a epoch of cosmic inflation. Both players win!")
    wins1 += 1
    wins2 += 1
    print()
    print(name1, "'s score:", wins1)
    print(name2, "'s score:", wins2)
    print()
    cont = input("Do you want to continue playing? ").lower()
    if cont not in valid_responses:
      break
    
  elif player2 == "a" and player1 == "a":
    print("The collision of two oceans of air produces a windstorm. Both players win!")
    wins1 += 1
    wins2 += 1
    print()
    print(name1, "'s score:", wins1)
    print(name2, "'s score:", wins2)
    print()
    cont = input("Do you want to continue playing? ").lower()
    if cont not in valid_responses:
      break
      
  elif player2 == "w" and player1 == "w":
    print("the collision of two water worlds producess staggering rogue waves. Both players win!")
    wins1 += 1
    wins2 += 1
    print()
    print(name1, "'s score:", wins1)
    print(name2, "'s score:", wins2)
    print()
    cont = input("Do you want to continue playing? ").lower()
    if cont not in valid_responses:
      break
      
  elif player2 == "e" and player1 == "e":
    print("Two techtonic plates of earth collide to produce a soaring mountain range. Both players win!")
    wins1 += 1
    wins2 += 1
    print()
    print(name1, "'s score:", wins1)
    print(name2, "'s score:", wins2)
    print()
    cont = input("Do you want to continue playing? ").lower()
    if cont not in valid_responses:
      break
      
  elif player2 == "f" and player1 == "f":
    print("The collision of two searing fires produces a scorching conflagration. Both players win!")
    wins1 += 1
    wins2 += 1
    print()
    print(name1, "'s score:", wins1)
    print(name2, "'s score:", wins2)
    print()
    cont = input("Do you want to continue playing? ").lower()
    if cont not in valid_responses:
      break

# all the ways player1 can lose
  elif player1 not in winning_moves and player2 == "s":
    print(name1, "'s use of", player1, "was absolutely annihilated by", name2, "'s unforgiving vacuum of spacetime!")
    wins2 += 1
    print()
    print(name1, "'s score:", wins1)
    print(name2, "'s score:", wins2)
    print()
    cont = input("Do you want to continue playing? ").lower()
    if cont not in valid_responses:
      break
 
  elif player1 not in winning_moves and player2 == "a":
    print(name1, "'s use of", player1, "was absolutely annihilated by", name2, "'s oceanic pressure of air!")
    wins2 += 1
    print()
    print(name1, "'s score:", wins1)
    print(name2, "'s score:", wins2)
    print()
    cont = input("Do you want to continue playing? ").lower()
    if cont not in valid_responses:
      break
  
  elif player1 not in winning_moves and player2 == "w":
    print(name1, "'s use of", player1, "was absolutely annihilated by", name2, "'s relentless churning of water!")
    wins2 += 1
    print()
    print(name1, "'s score:", wins1)
    print(name2, "'s score:", wins2)
    print()
    cont = input("Do you want to continue playing? ").lower()
    if cont not in valid_responses:
      break

  elif player1 not in winning_moves and player2 == "e":
    print(name1, "'s use of", player1, "was absolutely annihilated by", name2, "'s crushing weight of earth!")
    wins2 += 1
    print()
    print(name1, "'s score:", wins1)
    print(name2, "'s score:", wins2)
    print()
    cont = input("Do you want to continue playing? ").lower()
    if cont not in valid_responses:
      break
  
  elif player1 not in winning_moves and player2 == "f":
    print(name1, "'s use of", player1, "was absolutely annihilated by", name2, "'s blistering heat of fire!")
    wins2 += 1
    print()
    print(name1, "'s score:", wins1)
    print(name2, "'s score:", wins2)
    print()
    cont = input("Do you want to continue playing? ").lower()
    if cont not in valid_responses:
      break
  

# all the ways player2 can lose
  elif player2 not in winning_moves and player1 == "s":
    print(name2, "'s use of", player2, "was absolutely annihilated by", name1, "'s unforgiving vacuum of spacetime!")
    wins1 += 1
    print()
    print(name1, "'s score:", wins1)
    print(name2, "'s score:", wins2)
    print()
    cont = input("Do you want to continue playing? ").lower()
    if cont not in valid_responses:
      break
  
  elif player2 not in winning_moves and player1 == "a":
    print(name2, "'s use of", player2, "was absolutely annihilated by", name1, "'s oceanic pressure of air!")
    wins1 += 1
    print()
    print(name1, "'s score:", wins1)
    print(name2, "'s score:", wins2)
    print()
    cont = input("Do you want to continue playing? ").lower()
    if cont not in valid_responses:
      break
      
  elif player2 not in winning_moves and player1 == "w":
    print(name2, "'s use of", player2, "was absolutely annihilated by", name1, "'s relentless churning of water!")
    wins1 += 1
    print()
    print(name1, "'s score:", wins1)
    print(name2, "'s score:", wins2)
    print()
    cont = input("Do you want to continue playing? ").lower()
    if cont not in valid_responses:
      break
      
  elif player2 not in winning_moves and player1 == "e":
    print(name2, "'s use of", player2, "was absolutely annihilated by", name1, "'s crushing weight of earth!")
    wins1 += 1
    print()
    print(name1, "'s score:", wins1)
    print(name2, "'s score:", wins2)
    print()
    cont = input("Do you want to continue playing? ").lower()
    if cont not in valid_responses:
      break
      
  elif player2 not in winning_moves and player1 == "f":
    print(name2, "'s use of", player2, "was absolutely annihilated by", name1, "'s blistering heat of fire!")
    wins1 += 1
    print()
    print(name1, "'s score:", wins1)
    print(name2, "'s score:", wins2)
    print()
    cont = input("Do you want to continue playing? ").lower()
    if cont not in valid_responses:
      break
      
  else:
    print("Neither player used a valid element.")
    print()
    print(name1, "'s score:", wins1)
    print(name2, "'s score:", wins2)
    print()
    cont = input("Do you want to continue playing? ").lower()
    if cont not in valid_responses:
      break

