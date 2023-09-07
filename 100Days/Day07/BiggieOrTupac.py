print("So you think you like hip hop?") 
group = input("Who do you like more: Biggie or Tupac? ")
if group == "Biggie" or group == "biggie" or group == "smalls":
  print("Straight up! Sounds like you represent the East Coast.")
elif group == "Tupac" or group == "tupac" or group == "pac":
  print("Eyyy, the West Coast is where it's at!")
  favorite = input("What's his best song? ")
  if favorite == "Changes":
    print("Yo absolutely,", favorite, "is the best!")
  else:
    print("That's a great one!")
else:
  print("Who? We're talking about classic hip hop here.")