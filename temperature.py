def temperature(fahrenheit):
    kelvin = ((5/9) * (fahrenheit - 32) + 273.16)
    print(kelvin)

def main():
    fahrenheit = float(input("Enter a temperature in fahrenheit: "))
    temperature(fahrenheit)

main()