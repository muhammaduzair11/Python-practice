print("WELCOME TO PRIME NUMBER CHECKER")


num = int(input("Enter your Number: "))
prime_state = False

for x in range(2,num):
  if num % x != 0:
    prime_state = True
  else:
    prime_state = False
    break

if prime_state == True:
  print("The Number is Prime")

else:
  print("The Number is not Prime")