def temperature_converter():
    print("🌡️ Temperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    print("5. Fahrenheit to Kelvin")
    print("6. Kelvin to Fahrenheit")

    choice = input("Choose an option (1-6): ")

    try:
        temp = float(input("Enter temperature: "))

        if choice == "1":
            result = (temp * 9/5) + 32
            unit = "°F"
            valid = temp >= -273.15

        elif choice == "2":
            result = (temp - 32) * 5/9
            unit = "°C"
            valid = temp >= -459.67

        elif choice == "3":
            result = temp + 273.15
            unit = "K"
            valid = temp >= -273.15

        elif choice == "4":
            result = temp - 273.15
            unit = "°C"
            valid = temp >= 0

        elif choice == "5":
            result = (temp - 32) * 5/9 + 273.15
            unit = "K"
            valid = temp >= -459.67

        elif choice == "6":
            result = (temp - 273.15) * 9/5 + 32
            unit = "°F"
            valid = temp >= 0

        else:
            print("Invalid choice. Please select 1-6.")
            return

        if valid:
            print(f"Converted temperature: {result:.2f} {unit}")
        else:
            print("Invalid temperature: below absolute zero.")

    except ValueError:
        print("Please enter a valid number.")


temperature_converter()
