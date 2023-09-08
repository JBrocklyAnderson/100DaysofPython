import os

vowels = ["a", "e", "i", "o", "u", "y"]
firstSet = ["b", "c", "d", "f", "0", "1", ",", ".", "!", "-", "_", "?", "+"]
secondSet = ["g", "h", "j", "k", "2", "3", "@", "#", "$", "%", "^", "&", "="]
thirdSet = ["l", "m", "n", "p", "4", "5", "*", "(", ")", "[", "]", "{"]
fourthSet = ["q", "r", "s", "t", "6", "7", "}", "|", "/", "'", '"', ";"]
fifthSet = ["v", "w", "x", "z", "8", "9", ":", "<", ">", "`", "~", "—"]

pangram = "Jumping vortices dazzle while black quasars fix the night sky."

def colorPrinter(words):
  for letter in words:
    if letter.lower() in vowels:
      print("\033[36m", end = "")
    if letter.lower() in firstSet:
      print("\033[32m", end = "")
    if letter.lower() in secondSet:
      print("\033[34m", end = "")
    if letter.lower() in thirdSet:
      print("\033[31m", end = "")
    if letter.lower() in fourthSet:
      print("\033[35m", end = "")
    if letter.lower() in fifthSet:
      print("\033[33m", end = "")
    print(letter, end = "")
    print("\033[0m", end = "")

colorPrinter(pangram)
print()
print()
print("Enter your text below, press ENTER, and see the magic in action:")
print()
userInput = input("")
os.system("cls" if os.name == "nt" else "clear")
colorPrinter(userInput)
print()