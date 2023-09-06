print("Can you guess a randomly-generated positive whole number 1 and 1,000,000? The answer is... probably not... but go ahead and give it a shot!")
print()
import random
number = random.randint(1, 1000000)
guess_count = 0

while True:
  guess = int(input("Go on, take a guess: "))
  guess_count += 1
  if guess > number:
    print("Whoops, too high!")
  elif guess < number:
    print("Whoops, too low!")
  elif guess == number:
    print(f"Wow! You actually guessed a random number between 1 and 1,000,000; that's truly astonishing and you did it in only {guess_count} tries! Go sink some money into lottery tickets because you've beaten the universe.")
    break