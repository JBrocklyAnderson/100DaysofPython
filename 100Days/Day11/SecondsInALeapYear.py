print("How many seconds are in a year?")
print()
current_year = int(input("What year is it? "))
regular_year = 60 * 60 * 24 * 365
leap_year = 60 * 60 * 24 * 366
if current_year % 4 == 0:
  print(leap_year)
else:
  print(regular_year)