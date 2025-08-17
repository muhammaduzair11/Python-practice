print("Welocome to todo list in Python")

task = []

while True:
  i = 0
  print("1. Add Task \n2. View Tasks \n3. Remove Task \n4. Exit")
  option = int(input("Choose: "))
  if option == 1:
    task.append(input("Add Task: "))
  elif option == 2:
    for x in task:
      i = i + 1
      print(f"Task no {i}: {x}")
  elif option == 3:
    x = int(input("Remove task no: "))
    task.pop(x - 1)
  elif option == 4:
    break
  else:
    print("Error")

