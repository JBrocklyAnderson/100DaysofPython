def palindrome(sentence):
  raw = "".join(i for i in sentence if i.isalnum()).lower()
  if len(raw) <= 1:
    return True
  if raw[0] != raw[-1]:
    return False
  return palindrome(raw[1:-1])

print("Palindrome Checker rekcehC emordnilaP\n")
sentence = input("Give us a word or sentence to check:\n\n").strip().lower()
checkPalindrome = palindrome(sentence)
if checkPalindrome:
      print(f"\nYes, '{sentence.title()}' is a palindrome!")
else:
  print(f"\nNope, '{sentence.title()}' is not a palindrome.")