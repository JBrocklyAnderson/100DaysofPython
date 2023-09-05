print("How do you feel so far about Repl.it's hundred days of Python?")

for i in range(1, 31):
  feeling = input(f"How do you feel about Day {i}?: ")
  statement = f"You thought Day {i} was {feeling}."

  print(f"{statement:^62}")