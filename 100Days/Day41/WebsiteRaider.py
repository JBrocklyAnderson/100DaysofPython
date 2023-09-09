import os

# create a dictionary
webDict = {
  "name" : None,
  "URL" : None,
  "description" : None,
  "rating" : None
}

# append user inputs into the dictionary
webDict["name"] = input("Website Name:  ")
webDict["URL"] = input("URL:  ")
webDict["description"] = input("What is the website about?  ")
webDict["rating"] = input("How many * out of 5?  ")

# clear screen
os.system("cls" if os.name == "nt" else "clear")

# print dictionary keys and values
print("🌟 Website Rating 🌟")
print()
for key, value in webDict.items():
  print(f"\033[32m{key.capitalize()}\033[0m: \033[36m{value}\033[0m")