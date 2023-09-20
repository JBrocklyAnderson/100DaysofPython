import os, time, random

# screen-clearing function
def clearScreen():
  os.system("cls" if os.name == "nt" else "clear") ## clear screen on Windows ("nt") with "cls" or Linux/MacOS with "clear"

# Dictionary to map color names to their respective ANSI codes
def printColor(word, color):
  colors = {
      "reset": "\033[0m",
      "black": "\033[30m",
      "red": "\033[31m",
      "green": "\033[32m",
      "yellow": "\033[33m",
      "blue": "\033[34m",
      "purple": "\033[35m",
      "cyan": "\033[36m",
      "white": "\033[37m"
  }
  return print(f"{colors[color]}{word}{colors['reset']}")
  ## printColor("This is red", "red")