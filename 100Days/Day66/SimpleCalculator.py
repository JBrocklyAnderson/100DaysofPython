import tkinter as tk

# create the GUI window
window = tk.Tk()
window.title("Simple Calculator") 
window.geometry("300x150") 

# store the result or the current number being inputted
answer = 0

# store the previous number inputted before operators are used
lastNumber = 0

# initialize an empty operator variable to plug into the calculate function
operator = None

# store the numbers clicked on the calculator
def typeAnswer(value):
  global answer
  answer = f"{answer}{value}" ## add new number to previously pressed button
  answer = int(answer) ## cast both numbers together as a single integer
  hello["text"] = answer ## update answer variable

# store the operator to be used in the calculation
def calcAnswer(Operator):
  global answer, lastNumber, operator
  lastNumber = answer
  answer = 0
  if Operator == "+":
    operator = "+"
  elif Operator == "-":
    operator = "-"
  elif Operator == "*":
    operator = "*"
  elif Operator == "/":
    operator = "/"
  hello["text"] = answer

def calculate():
  global answer, lastNumber, operator
  print(f"{lastNumber}\t{answer}\t{operator}") ## print the calculation to the console to check if it's properly functioning
  if operator == "+":
    total = lastNumber + answer
  if operator == "-":
    total = lastNumber - answer
  if operator == "*":
    total = lastNumber * answer
  if operator == "/":
    total = lastNumber / answer
  answer = total ## calculate the total based on prior inputs
  hello["text"] = answer ## update answer

def clear():
  global answer, lastNumber, operator
  answer = 0
  lastNumber = 0
  operator = None
  hello["text"] = answer

hello = tk.Label(text = answer) ## display the result and inputted numbers above the buttons
hello.grid(row = 0, column = 1) ## place the text above the digit buttons

# add button for 1
one = tk.Button(text = "1", command = lambda:typeAnswer(1), width = 4, height = 1) ## use lambda to call typeAnswer() only when needed and not as soon as the button is created
one.grid(row = 1, column = 0)

# add button for 2
two = tk.Button(text = "2", command = lambda:typeAnswer(2), width = 4, height = 1)
two.grid(row = 1, column = 1)

# add button for 3
three = tk.Button(text = "3", command = lambda:typeAnswer(3), width = 4, height = 1)
three.grid(row = 1, column = 2)

# add button for 4
four = tk.Button(text = "4", command = lambda:typeAnswer(4), width = 4, height = 1)
four.grid(row = 2, column = 0)

# add button for 5
five = tk.Button(text = "5", command = lambda:typeAnswer(5), width = 4, height = 1)
five.grid(row = 2, column = 1)

# add button for 6
six = tk.Button(text = "6", command = lambda:typeAnswer(6), width = 4, height = 1)
six.grid(row = 2, column = 2)

# add button for 7
seven = tk.Button(text = "7", command = lambda:typeAnswer(7), width = 4, height = 1)
seven.grid(row = 3, column = 0)

# add button for 8
eight = tk.Button(text = "8", command = lambda:typeAnswer(8), width = 4, height = 1)
eight.grid(row = 3, column = 1)

# add button for 9
nine = tk.Button(text = "9", command = lambda:typeAnswer(9), width = 4, height = 1)
nine.grid(row = 3, column = 2)

# add button for 0
zero = tk.Button(text = "0", command = lambda:typeAnswer(0), width = 4, height = 1)
zero.grid(row = 4, column = 1)

# add button for +
add = tk.Button(text = "+", command = lambda:calcAnswer("+"), width = 4, height = 1)
add.grid(row = 1, column = 5)

# add button for -
subtract = tk.Button(text = "-", command = lambda:calcAnswer("-"), width = 4, height = 1)
subtract.grid(row = 2, column = 5)

# add button for *
multiply = tk.Button(text = "*", command = lambda:calcAnswer("*"), width = 4, height = 1)
multiply.grid(row = 3, column = 5)

# add button for /
divide = tk.Button(text = "/", command = lambda:calcAnswer("/"), width = 4, height = 1)
divide.grid(row = 4, column = 5)

# add button for =
equals = tk.Button(text = "=", command = calculate, width = 4, height = 1)
equals.grid(row = 2, column = 6)

# add a button to clear all inputs
clear = tk.Button(text = "C", command = clear, width = 4, height = 1)
clear.grid(row = 3, column = 6)

tk.mainloop()