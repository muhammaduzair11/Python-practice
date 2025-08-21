import requests

word = requests.get("https://random-word-api.herokuapp.com/word").json()[0]

guess = []
max_try = 7

for x in range(len(word)):
  guess.append("_ ")

print("WELCOME TO HANGMAN GAME")
print("Guess The Word\n")


while max_try > 0:
  for x in range(len(guess)):
    print(guess[x], end="")
  print(f"Lives Left: {max_try}")
  letter = input("\nGuess: ")

  if letter in word:
    for i in range(len(word)):
      if word[i] == letter:
        guess[i] = letter + " "
  else:
    max_try = max_try - 1

  if "_ " not in guess:
    print(f"Congrats, You Won! The Word was {word}")
    break

  if max_try == 0:
    print(f"The Word was: {word}")

