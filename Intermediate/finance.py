import json

print("WELCOME TO FINANCE TRACKER")

expenses = []

while True:
  print("1. Add New Expenses\n2. Show All Expenses\n3. Show Total Spent\n4. Show by category\n5. Delete an Expense\n6. Exit")


  option = int(input("Choose: "))

  if option == 1:
    category = input("Enter Category: ").lower()
    spent = float(input("Spent: "))
    note = input("Note: ")

    expense = {}
    expense["category"] = category
    expense["spent"] = spent
    expense["note"] = note

    expenses.append(expense)

  elif option == 2:
    for i, x in enumerate(expenses, start = 1):
      print(f"{i}. Category: {x["category"]}, Spent: {x["spent"]}, Note: {x["note"]}")

  elif option == 3:
    total_spent = 0
    for x in expenses:
      total_spent = total_spent + x["spent"]

    print(f"Total Spent = {total_spent}")

  elif option == 4:
    search_category = input("Search Category: ").lower()
    category_spent = 0
    for x in expenses:
      if x["category"] == search_category:
        category_spent = category_spent + x["spent"]
    
    print(f"Total Spent in {search_category} = {category_spent}")

  elif option == 5:
    del_category = input("Enter the category you want to delete: ")
    i = 0
    while i < len(expenses):
      if expenses[i]["category"] == del_category:
        del expenses[i]
      else:
        i += 1
    print(f"All expenses related to {del_category} has been Reomved")

  elif option == 6:
    break

  else:
    print("ERROR")

with open("finance.json", "w") as f:
    json.dump(expenses, f, indent=4)