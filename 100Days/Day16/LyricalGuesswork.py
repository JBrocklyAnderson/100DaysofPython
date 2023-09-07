print("Fill in the blank lyrics!")
print()
print("How many attempts will it take, I wonder...")
print("Here's a few hints. This is a hip hop song. There's both an internal and external rhyme scheme. None of your guesses should rhyme. Good luck!")
print()
print("There's a ___ going on / between the rich and the _____ / it's in the streets, world wide / ____seas and under oath")
attempts = 0 
while True:
  war = input("First blank? ")
  broke = input("Second blank? ")
  over = input("Third blank? ")
  attempts += 1
  if war == "war" and broke == "broke" and over == "over":
    break
  else:
    print("Not quite, try again!")
if attempts == 1:
  print("Awesome! You guessed it in only", attempts, "try!")
else:
  print("Awesome! You guessed it in only", attempts, "tries!")
print()
print("Credit to Braille for Keep[ing] On! (that's indeed the name of the song)")