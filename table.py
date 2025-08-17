print("WELCOME TO MULTIPLICATION TABLE GENERATOR")

table = int(input("Enter The Number You Want the Table Of: "))

for x in range(1,11):
  print(f"{table} x {x} = {table * x}")