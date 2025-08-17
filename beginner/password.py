import getpass
import string

print("WELCOME TO PASSWORD STRENGTH CHECKER")

password = getpass.getpass()

has_upper = any(char.isupper() for char in password)
has_number = any(char.isdigit() for char in password)
has_special_ch = any(char in string.punctuation for char in password)

if has_upper and has_number and has_special_ch:
  print("Your Password is strong")

else:
  print("Pasword is weak it must contain Uppercase, Number and special character")