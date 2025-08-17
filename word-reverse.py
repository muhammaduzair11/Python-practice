print("WELCOME TO WORD REVERSER")

word = input("Enter your word: ")
reversed = word[::-1] 

print(reversed)
if word == reversed:
  print("btch thats a palindrome")