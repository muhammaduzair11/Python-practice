import random

print("WELCOME TO STONE, PAPER, SCISSOR")
num_game = int(input("Best of : "))
elements = ["rock", "paper", "scissor"]
user_score = 0
computer_score = 0


for x in range(num_game):

  if user_score > (num_game/2) or computer_score > (num_game/2):
    break 
  while True:
    user_choice = input("Choose Rock, Paper or scissor: ").lower()
    if user_choice in elements:
      break

  computer_choice = random.choice(elements)

  if computer_choice == "rock":
    if user_choice == "paper":
      user_score += 1
      print(f"You Won. Computer choice was {computer_choice}\nScore: {user_score}-{computer_score}")
    elif user_choice == "scissor":
      computer_score += 1
      print(f"Computer Won. Computer choice was {computer_choice}\nScore: {user_score}-{computer_score}")
    else:
      user_score += 1
      computer_score += 1
      print(f"Draw. Computer Choice was {computer_choice}\nScore: {user_score}-{computer_score}")
  elif computer_choice == "paper":
    if user_choice == "scissor":
      user_score += 1
      print(f"You Won. Computer choice was {computer_choice}\nScore: {user_score}-{computer_score}")
    elif user_choice == "rock":
      computer_score += 1
      print(f"Computer Won. Computer choice was {computer_choice}\nScore: {user_score}-{computer_score}")
    else:
      user_score += 1
      computer_score += 1
      print(f"Draw. Computer Choice was {computer_choice}\nScore: {user_score}-{computer_score}")
  elif computer_choice == "scissor":
    if user_choice == "rock":
      user_score += 1
      print(f"You Won. Computer choice was {computer_choice}\nScore: {user_score}-{computer_score}")
    elif user_choice == "paper":
      computer_score += 1
      print(f"Computer Won. Computer choice was {computer_choice}\nScore: {user_score}-{computer_score}")
    else:
      user_score += 1
      computer_score += 1
      print(f"Draw. Computer Choice was {computer_choice}\nScore: {user_score}-{computer_score}")

if user_score > computer_score:
  print(f"Congrats. You Won!!! by {user_score}-{computer_score}")
elif computer_score > user_score:
  print(f"You Lost :) by {user_score}-{computer_score}")
else:
  print(f"Draw. You didnt win but you didnt lose either!! {user_score}-{computer_score}")

