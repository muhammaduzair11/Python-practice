import random

print("I am thinking of a number.")
random_num = random.randint(0,20)
attempts = 0

while 1:
  guess = int(input("Guess: "))
  attempts += 1

  if guess > random_num:
    print("TOO HIGH")

  elif guess < random_num:
    print("TOO LOW")

  elif guess == random_num:
    print("Btch YOu got it \nAttempts: ", attempts)
    break

  else:
    print("Error")