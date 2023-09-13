# import libraries
import os, time

# initialize empty container
pizzaOrders = []

# set prices
pizzaPrices = {
  "XL": 30.99,
  "L": 25.99,
  "M": 20.99,
  "S": 15.99,
  "P": 10.99
}

# store file contents to empty list
try:
  f = open("pizza.orders", "r")
  pizzaOrders = eval(f.read())
  f.close()
except Exception as errorType:
  print("ERROR: Unable to load pizza orders.\n")
  print(f"{errorType}\n")

# screen-clearing mechanism
def clearScreen():
  os.system("cls" if os.name == "nt" else "clear")

# function to add a pizza order
def addOrder():
  clearScreen()
  shopName = "🍕 The Leaning Tower 🗽\n"
  tagLine = "Our secret recipe is on a knead the dough basis.\n"
  print(f"{shopName:^50}\n{tagLine:^52}")
  
  name = input("\nName for the order?  ")
  size = input("What size pizza would you like (XL / L / M / SM / P)?  ").strip().upper()

  # prevent invalid inputs
  try:
    quantity = int(input("How many pizzas would you like?  "))
  except:
    print("Quantity must be a whole numerical character.")
    time.sleep(2)
    return addOrder()

  if size not in pizzaPrices:
    print("Invalid size.")
    time.sleep(2)
    return addOrder()

  # calculate cost of order
  cost = round((pizzaPrices[size] * quantity),2)

  # append order details to 2D list
  pizzaOrders.append([name, size, quantity, cost])
  print(f"Thanks {name}! {quantity} {size} pizzas will come out to ${cost}.")
  input("\nPress enter to continue.")

def viewOrder():
  clearScreen()
  shopName = "🍕 The Leaning Tower 🗽\n"
  tagLine = "Our secret recipe is on a knead the dough basis.\n"
  print(f"{shopName:^50}\n{tagLine:^50}")
  print("NAME | SIZE | QUANTITY | COST\n")
  for order in pizzaOrders:
    print(f"{order[0]} | {order[1]} | {order[2]} | ${order[3]}")
  input("\nPress enter to continue.")

while True:
  clearScreen()
  shopName = "🍕 The Leaning Tower 🗽\n"
  tagLine = "Our secret recipe is on a knead the dough basis."
  print(f"{shopName:^50}\n{tagLine:^50}\n")  
  menu = input("Add Order (1)\nView Order (2)\nExit (3)\n\n")

  if menu == "1":
    addOrder()
  elif menu == "2":
    viewOrder()
  elif menu == "3":
    break
  else:
    print("Invalid choice.")
    input("Press enter to continue.")

  # save the inputted orders
  f = open("pizza.orders", "w")
  f.write(str(pizzaOrders))
  f.close()