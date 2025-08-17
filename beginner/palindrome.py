print("WELCOME TO PALINDROME CHECKER")

word = input("Enter Word, Number or Phrase: ")
x = word.lower().replace(" ", "")

reversed = x[::-1]

if x == reversed:
  print("Its a Palindrome")
else:
  print("It isnt a Palindrome ;)")