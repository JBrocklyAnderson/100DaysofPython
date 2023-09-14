# recursive factorial function
def factorial(value):
  ## if n = 0, then n! = 1
  ## setting a base/end condition to work towards
  if value == 0:
    return 1
  
  else:  ## n! = n * (n - 1)
    return value * factorial(value - 1) ## working towards the base condition

number = int(input("Enter a number to compute its factorial:  "))
print(factorial(number)) ## having the function call itself