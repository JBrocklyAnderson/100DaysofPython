print("Welcome to my affirmation generator. Prepare yourself as the generator lights a fire under your feet!")
print()
print("*Note: you may not always get the appropriate phrasing when using this generator and it's very nerdy.")
print()
name = input("Let's get a little personal——what's your name? ")
print("Great to meet you", name, "!")
goal = input("What's your plan for today? ")
print("Sounds amazing!")
day = input("What day of the week is it? ")
if day == "Monday" or day == "monday":
  print("Well,", name, ", this", day, "you're going to have a stellar time", goal, "! It's almost Friday, I promise.")
elif day == "Tuesday" or day == "tuesday":
  print("I can't think of a better way to spend a", day, "than", goal, ",", name, ". Go get 'em tiger!")
elif day == "Wednesday" or day == "wednesday" or day == "Hump Day" or day == "hump day" or day == "Hump day":
  print("Hell yes it's", day, "! You're going to have best freakin'", day, goal, "ever", name, "!")
elif day == "Thursday" or day == "thursday":
  print(goal, "?! Sounds like a top-notch recipe for a chill", day, ",", name, "!")
elif day == "Friday" or day == "friday":
  print(day, "'s the best day of the week, no doubt! Start of the weekend, you get to go", goal, ", the whole nine yards... Could", name, "even ask for more?")
elif day == "Saturday" or day == "saturday":
  print("The week's hardly over on a", day, ", get out there, kick some ass, take some names, and go", goal, ",", name, "!")
elif day == "Sunday" or day == "sunday":
  print("Welcome to", day, ",", name, ", I can see an awesome time", goal, ". Carpe diem and seize the means!")
else:
  print("C'mon,", name, ", you're bustin' my billiards, here. I'm trying to hype you up, friend! Let's take it back around again.")