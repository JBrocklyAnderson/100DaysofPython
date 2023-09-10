import random, os, time

# screen-clearing function
def clearScreen():
  os.system("cls" if os.name == "nt" else "clear")

def createCard():
    # generate, shuffle, and sort 24 numbers
    def genBingoNum():
        numbers = list(range(1,91))
        random.shuffle(numbers)
        return sorted(numbers[:25])

    # set the function equal to a variable
    bingoNum = genBingoNum()
    
    # extract numbers from bingoNum
    bingoCard = [bingoNum[num:num+5] for num in range(0, len(bingoNum), 5)]
    
    # replace center tile with "BINGO"
    bingoCard[2][2] = "BINGO"

    return bingoCard

bingoCard = createCard()

# define a title
title = "🎰 LET'S PLAY BINGO BLACKOUT! 🎰"
# define tile width
width = 10
# define the total length of a row
rowLength = width * len(bingoCard[0]) + (len(bingoCard[0]) - 1)

def cardPrint():
    # print a centered title
    print(f"\033[32m{title:^{rowLength}}\033[0m")
    
    # print the card
    print("\033[36m") # make it cyan
    for row in bingoCard: 
        formatted_row = [f"{item:^{width}}" for item in row] # center every item in every row
        print("|".join(formatted_row)) # separate
        print("-" * (width * len(row) + (len(row) - 1)))
    print("\033[0m")

def checkWin():
  countX = sum([row.count('X') for row in bingoCard])
  return countX == 24 # returns True when countX == 24

def game():
  while True:
    clearScreen()
    cardPrint()
    try:
      userInput = int(input("What's the next BINGO number (1-90):\n\n"))
      if 1 <= userInput <= 90: 
        for row in bingoCard: # check every row
          if userInput in row: # check every item
            index = row.index(userInput) # index the item
            row[index] = "X" # change it to X
            if checkWin(): # if checkWin == True
              clearScreen()
              cardPrint()
              print(f"\n\033[32mCongratulations! You've won BINGO BLACKOUT!")
              return
        print(f"\nNumber {userInput} marked!")
      else:
        print("\n\033[31mInvalid input. Please enter a number between 1 and 90.\033[0m")
        time.sleep(2.75)
    except:
      print("\n\033[31mInput must be a number. Try again.\033[0m")
      time.sleep(1.5)

game()
