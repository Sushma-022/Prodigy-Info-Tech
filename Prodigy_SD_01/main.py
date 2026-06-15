temperature = int(input("Enter the temperature:"))
degree = input("Enter the degree(C,F,K):")
if degree == "C" :
    Celsius_to_Fahrenheit = (temperature * 9/5) + 32
    Celsius_to_Kelvin = temperature + 273.15
    print("Celsius to Fahrenheit:" ,Celsius_to_Fahrenheit )
    print("Celsius to Kelvin:", Celsius_to_Kelvin)
elif degree == "F" :
    Fahrenheit_to_Celsius = (temperature - 32) * 5/9
    Fahrenheit_to_Kelvin = (temperature - 32) * 5/9 + 273.15
    print("Fahrenheit to Celsius:",  Fahrenheit_to_Celsius)
    print("Fahrenheit to Kelvin:", Fahrenheit_to_Kelvin)
elif degree == "K" :
    Kelvin_to_Celsius = temperature - 273.15
    Kelvin_to_Fahrenheit = (temperature - 273.15) * 9/5 + 32
    print("Kelvin to Celsius:", Kelvin_to_Celsius)
    print("Kelvin to Fahrenheit:", Kelvin_to_Fahrenheit)
else:
    print("Enter valid temperature and degree")