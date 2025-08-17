print("WELCOME TO CALCULATOR")

num1 = float(input("Enter First Number: "))
num2 = float(input("Enter Second Number: "))

operation = input("Enter desired operation +,-,/,* :  ")

if operation == "+":
  print(f"Result: {num1 + num2}")

elif operation == "-":
  print(f"Result: {num1 - num2}")

elif operation == "/":
  print(f"Result: {num1 / num2}")

elif operation == "*":
  print(f"Result: {num1 * num2}")

else:
  print("Error")