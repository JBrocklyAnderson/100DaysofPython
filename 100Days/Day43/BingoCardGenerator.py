import random

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

# define a title
title = "🎰 LET'S PLAY BINGO! 🎰"

# define tile width
width = 10

# define the total length of a row
rowLength = width * len(bingoCard[0]) + (len(bingoCard[0]) - 1) * 3 # n tiles - 1, then multiply by 3 because the separator " | " contains three spaces 

# print a centered title
print(f"\033[32m{title:^{rowLength}}\033[0m")

# print a cyan table
print("\033[36m")
for row in bingoCard:
  formatted_row = [f"{item:^{width}}" for item in row]
  print(" | ".join(formatted_row))
  print("-" * (width * len(row) + (len(row) - 1) * 3))
print("\033[0m")