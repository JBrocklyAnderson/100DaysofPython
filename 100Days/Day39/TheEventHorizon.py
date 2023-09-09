import random, os, time

def clearScreen():
  os.system("cls" if os.name == "nt" else "clear")

def playGame():
  # creating a word list
  wordList = ["cosmic", "galaxy", "nebula", "planet", "meteor", "comets", "quasar", "pulsar", "gravity", "eclipse", "stellar", "lunar", "orbit", "black hole", "solar", "neutron", "constellation", "celestial", "universe", "interstellar", "telescope", "radiation", "asteroid", "milky way", "andromeda" "starlight", "satellite", "cluster", "galactic", "expansion", "supernova", "observatory", "spectrum", "gravity", "spaceship", "equinox", "sunspot", "cosmology", "dark matter", "relativity", "parallax", "lightyear", "magnitude", "aurora", "apogee", "elliptic", "", "rotation", "ecliptic", "big bang", "inflation", "extrasolar", "magnetar", "gamma ray burst", "string theory", "extraterrestrial", "kardashev scale", "schwarzchild radius", "wormhole", "alcubierre drive", "solar flare", "coronal mass ejection", "supergiant", "stellar nursery", "hyperspace", "time dilation", "absolute zero", "starship", "moonrise", "sunquake", "redshift", "twilight", "zenithal", "sidereal", "infinity", "eternity", "starport", "darkstar", "protosun", "skyglow", "callisto", "ganymede", "einstein", "hawkings", "jupiter", "saturn", "enceladus", "titan", "ceres", "hyperdrive", "warp speed", "multiverse", "panspermia", "voyager", "sputnik", "mercury", "neptune", "uranus", "kuiper belt", "brown dwarf", "main sequence"]
  
  # keep track of letters already chosen
  chosenLetters = []
  
  # obtaining a random word from the list
  password = random.choice(wordList)
  
  # give the user 10 chances
  countdown = 15
  
  # opening screen
  print("THE EVENT HORIZON")
  time.sleep(2)
  clearScreen()
  
  # scene setting
  print("STARDATE: 12023") 
  time.sleep(2)
  clearScreen()
  print("You're a starship mechanic in an instellar emergency with only minutes left to live.")
  print()
  print("The hull deteriorated slowly over many months by the lightning impact of trillions of particles of dust, but this was all accounted for in the design.")
  print()
  print("Unfortunately, a slightly larger grain of sand must have found it's way from out of nowhere to pierce the weakened metal. Suddenly, the captain is sucked out into the frozen vacuum of space. The crew are stuck in cryogenic chambers. It's up to you now.")
  print()
  print("You need to guess the ship's password in order to access the escape pods. You can guess one letter at a time, but every time you guess it takes one minute. You have 15 minutes left...")
  
  while countdown > 0:
    # prompt user for a guess
    print()
    print(f"{countdown} minutes to system failure!")
    print()
    guess = input("What's your guess, Captain?\n").lower()
    clearScreen()
    
    # double check for novelty
    if guess in chosenLetters:
      print("You've tried that before, Captain! We're running out of time...")
      print()
      print(f"Already Guessed: {', '.join(chosenLetters)}")
      print()
      countdown -= 1
      continue
  
    # keep track of guesses
    chosenLetters.append(guess)
  
    # use the guess if it's in the password
    if guess in password:
      print("Way to go, Captain! We're one step closer to safety...")
      print()
      print(f"Already Guessed: {', '.join(chosenLetters)}")
      print()
      countdown -= 1
    else:
      print("Oh no! Guess again, Captain, you're our last hope...")
      print()
      print(f"Already Guessed: {', '.join(chosenLetters)}")
      print()
      countdown -= 1
  
    solved = True
    for i in password:
      if i in chosenLetters:
        print(i, end = "")
      else:
        print("_", end = "")
        solved = False
    print()
  
    
    if solved:
      if countdown == 1:
        print()
        print(f"Captain, you did it! You hacked the starship, which gave you access to the escape pod's control panel. With just {countdown} minute to spare, you slide the crew into the pod, close the door, shoot off into space, and watch the ship disintegrate from an ever-safer distance. Destination: Earth. Status: Alive.")
      else:
        print()
        print(f"Captain, you did it! You hacked the starship, which gave you access to the escape pod's control panel. With just {countdown} minutes to spare, you slide the crew into the pod, close the door, shoot off into space, and watch the ship disintegrate from an ever-safer distance. Destination: Earth. Status: Alive.")
      break
  
  # once the minutes fall to 0
  else:
    print()
    print(f"'\033[31m{password}\033[0m' has eluded us...")
    print()  
    print("A warbling begins—slowly, at first, but its oscillations quicken their frenzy until—BOOM! All you can see is shrapnel, wiring, and the alien beauty of the infinite cosmos. All you can feel is the icy grip of an eternal abyss.")

playGame()