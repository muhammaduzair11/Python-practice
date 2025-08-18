import json

print("WELCOME TO CONTACT BOOK")

contacts = {}

try:
    with open("contacts.json", "r") as f:
        contacts = json.load(f)
except FileNotFoundError:
    contacts = {}

while True:
  print("1. Add New Number\n2. Search a Contact\n3. Delete a Contact\n4. Show All Contacts\n5. Exit")
  choice = int(input("Choose: "))

  if choice == 1:
    name = input("Enter the Name you want to save: ")
    number = input("Their Phone no: ")

    contacts[name] = number
    

  elif choice == 2:
    find = input("Enter Name: ")

    if find in contacts:
      print(f"The Number of {find} is {contacts[find]}")
    else:
      print("Contact does not exist")

  elif choice == 3:
    delete = input("Enter the contact name you want to delete: ")

    if delete in contacts:
      del contacts[delete]
      print("Contact Succesfully Deleted")
    else:
      print("Contact dosnt exist")

  elif choice == 4:
    for name, number in contacts.items():
      print(f"{name} : {number}")


  elif choice == 5:
    break

  else:
    print("Error")

with open("contacts.json", "w") as f:
    json.dump(contacts, f, indent=4)