print("\033[32;40mWelcome to the Star Wars Universe!\033[0m")
print("""\033[32;40m
              What                
           would your             
         name have been           
       a long time ago in         
     a galaxy far, far away?      \033[0m""")
print()

first = input("\033[32;40mWhat's your first name in stardate 12023?\n\033[0m").capitalize()
print()
last = input("\033[32;40mWhat's your last name in stardate 12023?\n\033[0m")
print()
maiden = input(f"\033[32;40m{first} {last}, what is your mother's maiden name?\n\033[0m").capitalize()
print()
city = input("\033[32;40mWhere was your mother born?\n\033[0m")
print()

def nameSlicer():
  # assemble the new first name
  first3 = first[:3]
  last3 = last[:3].lower()
  firstName = f"{first3}{last3}"
  
  # assemble the new last name
  maiden3 = maiden[:3]
  city2 = city[-2:]
  lastName = f"{maiden3}{city2}"

  # print the new full name
  newName = print(f"\033[32;40m{first} {last}, your Star Wars name is {firstName} {lastName}!\033[0m")
  return newName  

# call the function
nameSlicer()