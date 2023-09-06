import random 

def infinity_dice():
  affirmative_answers = ["yes", "yeah", "sure", "why not", "i guess", "sounds good", "sounds great", "sounds groovy", "dope", "hell yeah", "ok", "okay", "for sure", "definitely", "absolutely", "you got it", "tight", "sick", "fire"]
  while True:
    sides = int(input("How many sides should your two dice have? "))
    roll1 = random.randint(1, sides)
    roll2 = random.randint(1, sides)
    print(f"Your {sides}-sided dice rolled a {roll1 + roll2}")
    
    reroll = input("You want to roll again? ").lower()
    if reroll not in affirmative_answers:
      break

infinity_dice()
