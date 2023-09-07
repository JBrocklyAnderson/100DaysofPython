print("Let's make a multiplication table with any number you choose! Don't worry, I'll do the heavy lifting 🦾")
print()
# getting user input
number = int(input("What number do you want to practice multiplying? ")) 

# initializing user score to 0
score = 0 

# looping through numbers 1 to 10
x = range(1, 11)
for i in x:
  correct_answer = i * number
  user_answer = int(input(f"What is the product of {number} x {i}? "))
  if user_answer == correct_answer:
    print("Great Work!")
    score += 1
  else:
    print(f"Not quite, the correct answer was {correct_answer}.")

print()
print(f"You scored {score} out of 10.")
if score == 10:
  print("🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉") # printing a congratulatory emoji string for a perfect score


