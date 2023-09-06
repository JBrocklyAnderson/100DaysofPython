# creating a subroutine
def login_system():
  correct_username = "some_username"
  correct_password = "some_password"
  authenticated = False # falsifying user authentification

  # setting a loop to request for account details
  while not authenticated:
    username = input("What is your username?: ")
    password = input("What is your password?: ")

    # setting conditions for authentification
    if username == correct_username and password == correct_password:
      print()
      print("Welcome to Replit!")
      authenticated = True # authentication user
    else:
      print()
      print("I'm sorry, the system could not verify your account information. Please try again.")
      print()

login_system() # calling the subroutine