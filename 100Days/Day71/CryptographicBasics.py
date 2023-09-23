import os, time, random ## useful libraries
from replit import db ## access Repl.it's database
from getpass import getpass as security ## hide user input

# screen-clearing subroutine
def cls():
  os.system("cls" if os.name == "nt" else "clear")

# subroutine used to "create account"
def newUser():
  newUN = security("Enter a username:   ").strip()
  newPW = security("Enter a password:   ").strip()
  salt = random.randint(1, 1000000) ## randomizing salt values
  saltedPW = f"{newPW}{salt}" ## appending the salt to chosen password
  hashed = hash(saltedPW) ## hashing the new password
  db[newUN] = {"password": hashed,
                 "salt": salt} ## storing this information in the database
  print(f"\nCongratulations {newUN}! Your account has been created successfully.")
  input("\nPress enter to continue...")
  
# authenticating login information
def login():
  while True:
    UNask = security("Enter your username:   ").strip()
    PWask = security("Enter your password:   ").strip()
    
    if UNask in db: 
      salt = db[UNask]["salt"] ## grabbing salt value from specific user if they already have an "account"
      saltedPW = f"{PWask}{salt}" ## appending registered salt value to their password guess
      hashPW = hash(saltedPW) ## hashing the new password
  
      if hashPW == db[UNask]["password"]: ## checking the hashed password-salt against info stored in the database
        print(f"\nLogin Successful! Welcome {UNask}.")
        time.sleep(3)
        return
      else:
        print("\nLogin unsuccessful.\n")
        input("Press enter to return to menu.")
        return
    else:
      print("\nLogin unsuccessful.\n")
      input("Press enter to try again.")
      return

while True:
  cls()
  menu = input("Password Login System\n\n1. Create Account\n2. Login\n\n").strip()
  if menu == "1":
    cls()
    newUser()
  elif menu == "2":
    cls()
    login()
  else:
    print("\nInvalid option.")
    time.sleep(2)