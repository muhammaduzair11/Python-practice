print("WElCOME TO TEMPARATURE CONVERTER")
option = int(input("Choose \n 1. Celsius to Farenheit \n 2. Farenheit to Celsius \n =>"))

if option == 1:
  tempInCelsius = float(input("Enter Temparature in Celsius: "))
  tempInFarenheit = (tempInCelsius * 9/5) + 32
  print("Temparature in Farenheit would be " , tempInFarenheit)

elif option == 2:
  tempInFarenheit = float(input("Enter Temparature in Farenheit: "))
  tempInCelsius = (tempInFarenheit - 32) * 5/9
  print("Temparature in Celsius will be: " , tempInCelsius)