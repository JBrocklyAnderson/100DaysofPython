import os, time
listOfEmail = []

def prettyPrint():
  os.system("clear") 
  print("listofEmail") 
  print()
  for index in range(len(listOfEmail)):
    print(f"{index}: {listOfEmail[index]}") 
  time.sleep(3)

def spam():
  for email in listOfEmail[:min(10, len(listOfEmail))]:
    os.system("clear")
    print(f"""
Dear {email},

In these unprecedented times, where the world thirsts and nature's taps run dry, {company} is honored to present an unparalleled opportunity just for you!

🌟 Introducing our Limited-Edition AquaElixir Bottle! 🌟

Crafted with meticulous precision, each drop in our AquaElixir collection hails from the last untouched springs on Earth. You're not just sipping water – you're experiencing history, luxury, and rarity combined.

🔥 Why Choose LiquidGold's AquaElixir? 🔥

🌍 Eco-Packaging: Crafted from materials more durable than the environment.
💎 Diamond Filtered: Because regular carbon filtration is too mainstream.
🌟 Membership Exclusive: Access to our {company} Lounges, located in the last green spots on Earth.

For a limited time, enjoy a 20% discount on your first purchase with code: GOLDENLUXE2123.

💡 Did You Know? 💡
The average person might find water to be a basic necessity, but our clients know better. Join the ranks of the privileged and understand why we say: "Water is the new gold, and we're its sole brokers."

Don't miss out on this golden opportunity. Remember, in a world where hydration is the height of luxury, {company} ensures you're always on top.

👉 Order Now and Dive into Opulence!

{tagline}

The {company} Team
""")
    time.sleep(3)

while True:
  company = "LiquiGold LLC"
  tagline = "Drink today, for tomorrow is uncertain!"
  print(company)
  print()
  menu = input("1. Add email\n2: Remove email\n3. Show emails\n4. Send emails\n> ")
  if menu == "1":
    print()
    email = input("Email > ")
    listOfEmail.append(email)
  elif menu =="2":
    email = input ("Email > ")
    if email in listOfEmail:
      listOfEmail.remove(email)
  elif menu == "3":
    prettyPrint()
  elif menu == "4":
    spam()

  os.system("clear")