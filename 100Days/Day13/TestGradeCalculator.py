print("Grade Calculator")
print()
possible = float(input("How many points could you possibly have gotten? "))
actual = float(input("How many points did you actually get? "))
grade = round((actual / possible) * 100, 2)
if grade >= 90:
  print("Congratulations, you received a %", grade, ", which is an Amazing A!")
elif grade < 90 and grade >= 80:
  print("Great! You got a %", grade, ", which is a solid B!")
elif grade < 80 and grade >= 70:
  print("That's alright. A %", grade, "is a casual C. I know you can do better though.")
elif grade < 70 and grade >= 60:
  print("A D is honestly devastating. %", grade, "isn't great at all. Looks like you need to study more efficiently.")
else:
  print("With a %", grade, "you run the real risk of flunking out. F doesn't mean 'fantastic'.")