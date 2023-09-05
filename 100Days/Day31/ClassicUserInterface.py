def print_color(word, color):
    # Create a dictionary to map color names to their respective ANSI codes
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
  return f"{colors[color]}{word}{colors['reset']}"

# design the 1st interface
title = (
  print_color("=", "red") +
  print_color("=", "white") +
  print_color("=", "blue") +
  print_color(" ", "reset") +
  print_color("Music App", "yellow") +
  print_color(" ", "reset") +
  print_color("=", "blue") +
  print_color("=", "white") +
  print_color("=", "red")
)

radio = (
  print_color("🔥🎶   ", "reset") +
  print_color("Radio Gaga", "white")
)

band = (print_color("Queen", "yellow"))

# separate the controls with vertical tabs
control = (
  print_color("PREV  ", "white") + "\v" +
  print_color("NEXT  ", "green") + "\v" +
  print_color("PAUSE", "purple")
)

# print and align accordingly
print(f"{title:>107}")
print()
print(radio)
print(f"{band:^28}")
print()
print()
print(control)

# -----------------------------
print()
print()
print(print_color("-----------------------------------------------", "cyan"))
print()
print()  
# design the 2nd interface
welcome = print_color("WELCOME TO", "white")

armbook = print_color("--    ARMBOOK    --", "blue")

intro1 = print_color("Definitely not a rip off of", "yellow")
intro2 = print_color("a certain other social", "yellow")
intro3 = print_color("networking site.", "yellow")

honest = print_color("Honest.", "red")

username = print_color("Username: ", "white")
password = print_color("Password: ", "white")

print(f"{welcome:^50}")
print(f"{armbook:^50}")
print()
print(f"{intro1:>45}")
print(f"{intro2:>45}")
print(f"{intro3:>45}")
print()
print(f"{honest:^50}")
print()
print(f"{username:^52}")
print(f"{password:^52}")
