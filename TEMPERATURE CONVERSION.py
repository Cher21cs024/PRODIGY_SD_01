def celsius_to_fahrenheit(celsius):
    fahrenheit = celsius * 9/5 + 32
    return fahrenheit

def celsius_to_kelvin(celsius):
    kelvin = celsius + 273.15
    return kelvin

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def fahrenheit_to_kelvin(fahrenheit):
    kelvin = (fahrenheit + 459.67) * 5/9
    return kelvin

def kelvin_to_celsius(kelvin):
    celsius = kelvin - 273.15
    return celsius

def kelvin_to_fahrenheit(kelvin):
    fahrenheit = kelvin * 9/5 - 459.67
    return fahrenheit

def main():
    print("Temperature Converter between Celsius, Fahrenheit, and Kelvin\n")
    temperature = float(input("Enter the temperature value: "))
    original_unit = input("Enter the original temperature unit (C, F, K): ").upper()

    if original_unit == 'C':
        celsius = temperature
        fahrenheit = celsius_to_fahrenheit(celsius)
        kelvin = celsius_to_kelvin(celsius)
        print(f"{celsius} degrees Celsius is equal to:")
        print(f"{fahrenheit} degrees Fahrenheit")
        print(f"{kelvin} Kelvin")
    
    elif original_unit == 'F':
        fahrenheit = temperature
        celsius = fahrenheit_to_celsius(fahrenheit)
        kelvin = fahrenheit_to_kelvin(fahrenheit)
        print(f"{fahrenheit} degrees Fahrenheit is equal to:")
        print(f"{celsius} degrees Celsius")
        print(f"{kelvin} Kelvin")
    
    elif original_unit == 'K':
        kelvin = temperature
        celsius = kelvin_to_celsius(kelvin)
        fahrenheit = kelvin_to_fahrenheit(kelvin)
        print(f"{kelvin} Kelvin is equal to:")
        print(f"{celsius} degrees Celsius")
        print(f"{fahrenheit} degrees Fahrenheit")
    
    else:
        print("Invalid input! Please enter C, F, or K for the unit.")

if __name__ == "__main__":
    main()
