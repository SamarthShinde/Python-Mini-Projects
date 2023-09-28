def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def convert_temperature():
    temperature = float(input("Enter the temperature value: "))
    unit = input("Enter the unit of measurement (C for Celsius, F for Fahrenheit): ")

    if unit.upper() == 'C':
        converted_temperature = celsius_to_fahrenheit(temperature)
        converted_unit = 'Fahrenheit'
    elif unit.upper() == 'F':
        converted_temperature = fahrenheit_to_celsius(temperature)
        converted_unit = 'Celsius'
    else:
        print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
        return

    print(f"The temperature is {converted_temperature:.2f} {converted_unit}.")

# Call the function to convert the temperature
convert_temperature()
