print("Can you guess what positive whole number I'm thinking of between 0 and 100?")
print()
number = 58
guess_count = 0

while True:
  guess = int(input("Go on, take a guess: "))
  guess_count += 1
  if guess > 58:
    print("Whoops, too high!")
  elif guess >= 0 and guess < 58:
    print("Whoops, too low!")
  elif guess == 58:
    print(f"Congrats! You guessed my number in {guess_count} tries!")
    break
  elif guess < 0:
    print("You've gone too low.")
    exit()