import requests, os, time
from replit import db

def cls(): ## screen-clearing function
  os.system("cls" if os.name == "nt" else "clear")

while True: ## make a continuous interface
  cls()
  result = requests.get("https://icanhazdadjoke.com/", headers={"Accept": "application/json"}) ## grab random joke
  joke = result.json() ## read the data in JSON
  
  jk = joke["joke"]
  id = joke["id"]
  print(jk)
  
  answer = input("\nWhat next?\n\n1. Save the joke\n2. Load saved jokes\n3. Get new joke\n\n").strip()
  if answer == "1":
    db[id] = jk ## save the joke to the database
    print("\nJoke saved successfully!")
    time.sleep(1.5)
  elif answer == "2":
    cls()
    print("A List of All Your Jokes\n")
    keys = db.keys() ## grab keys from the database
    order = 0 ## set order count to 0
    for key in keys:
      result = requests.get(f"https://icanhazdadjoke.com/j/{key}", headers={"Accept": "application/json"}) ## call specific joke ID
      joke = result.json() ## read the data in JSON
      order +=1 ## create an order for the list of jokes
      print(f"{order}. {joke['joke']}\n") ## print list
    input("\nPress enter to continue")
  elif answer == "3":
    continue
  else:
    input("Invalid entry. Press enter to try again.")