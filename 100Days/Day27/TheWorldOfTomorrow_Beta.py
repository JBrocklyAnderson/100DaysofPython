import random, os, time

# introducing an opening screen
print("The World of Tomorrow")
time.sleep(2)
os.system("clear")

# generating a character's name and type
def character():
  char_name = input("Name your Legend:\n")
  print()
  char_type = input("Who are they? (Human, Android, Cyborg, Sentient Nanobot Cloud, Transhuman, AI, Transformer, Genetic Experiment, etc.):\n")
  print()
  return char_name, char_type

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

# obvious and secret affirmations
affirmatives = ["yes", "yeah", "sure", "why not", "i guess", "sounds good", "sounds great", "sounds groovy", "dope", "hell yeah", "ok", "okay", "for sure", "definitely", "absolutely", "you got it", "tight", "sick", "fire"]

# creating the main menu
while True:
  # clearing the main menu
  os.system("clear")
  print("Welcome to the World of Tomorrow")
  print()
  char_name, char_type = character()
  health = health_stat()
  strength = strength_stat()
  
  print("A Legend Grows...")
  print()
  print(f"They go by the name of {char_name}. Rumor has it they're a {char_type}.")
 
  # printing different messages based on the randomized stats generated
  if health >= 23:
    print()
    print(f"At a health level of {health}, they were endowed with a strong vitality to begin their epic journey to save the world.")
  elif health >= 11 and health < 23:
    print()
    print(f"Their vitality will need a little work, but at a health level of {health}, they'll grow into an iconic legend in due time.")
  else:
    print()
    print(f"Before beginning their epic journey, they'll have to work extra hard at developing their vitality, which sits at a meager health level of {health}.")
  
  if strength >= 24:
    print()
    print(f"{char_name} is incredibly strong. With a strength level of {strength}, nothing shall stand in their path.")
  elif strength >= 12 and strength < 24:
    print()
    print(f"{char_name} isn't the weakest link in the chain, but they aren't the strongest either. At a strength level of {strength}, they'll need to train even harder if they want to survive.")
  else:
    print()
    print(f"With a strength of {strength},{char_name} is barely strong enough to lift their limbs. Before becoming the powerful legend that can save the World of Tomorrow, they'll have no choice but to train or die.")

  # pausing the reinitialization prompt
  time.sleep(5)
  print()
  new_character = input("Do you want to create a new character? ").lower()
  if new_character in affirmatives:
    continue