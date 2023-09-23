import os
from getpass import getpass as security

def cls():
  os.system("cls" if os.name == "nt" else "clear")

admin = os.environ["admin"]
adminPass = os.environ["adminPass"]
norm = os.environ["norm"]
normPass = os.environ["normPass"]

while True:
  cls()
  username = security("Enter username:  ")
  password = security("Enter password:  ")
  if username == admin and password == adminPass:
    print("\nWelcome Admin!")
    break
  elif username == norm and password == normPass:
    print("\nWelcome User!")
    break
  else:
    print("\nYou're account could not be identified.\n")
    input("Press enter to try again.")