import os, time

def clearScreen():
  os.system("cls" if os.name == "nt" else "clear")

# imitate calculation time
def falseLoad():
  # use loop to imitate load time 
  for n in range(5): # repeat load loop 
    print("🌟 Current Leader 🌟")
    string = "\nAnalyzing high scores"
    print(string, end = "", flush = True)
    for dot in range(3): # repeat load ellipses
      time.sleep(0.25)
      print(".", end = "", flush = True)
    time.sleep(0.25)
    clearScreen()

# print program
def printProgram():
  falseLoad()
  print("🌟 Current Leader 🌟")
  print("\nJust kidding. The calculation doesn't take that long to load.")
  print(f"\nHighest Score goes to {maxScore[0]}: {maxScore[1]:,}")
  
f = open("high.score", "r")

maxScore = f.readline().strip().split()
maxScore[1] = int(maxScore[1])

while True:
  contents = f.readline()
  if contents == "":
    break
  name, score = contents.split()
  score = int(score)

  if score > maxScore[1]:
    maxScore = [name, score]
  
f.close()

printProgram()

