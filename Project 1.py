# Make the conversion

# fahrenheit to celcius
def fahrenheit_to_celsius(f):
    return (f-32) * 5 / 9
# pounds to kg
def pounds_to_kg(p):
    return p * 0.453592
# feet to meters
def feet_to_meters(ft):
    return ft * 0.3048
# miles to kilometers
def miles_to_km(m):
    return m * 1.60934
# galons to liter
def gallons_to_liters(g):
    return g * 3.78541

# display the options
while True:
    print("Enter your task")
    print("1: Fahrenheit to Celsius")
    print("2: Pounds to Kilograms")
    print("3: Feet to Meters")
    print("4: Miles to Kilometers")
    print("5: Gallons to Liters")
    print("0: To quit")

    choice = int(input("Enter your choice (0-5): "))

    if choice == 0:
        print("See you next time!")
        break
    elif choice == 1:
        temp_f = float(input("Enter temperature in fahrenheit: "))
        print(f"Result: {temp_f}F is {fahrenheit_to_celsius(temp_f)}C")
    elif choice == 2:
        weight_lb = float(input("Enter weight in pounds: "))
        print(f"Result: {weight_lb}lb is {pounds_to_kg(weight_lb)}kg")
    elif choice == 3:
        height_feet = float(input("Enter height in feet: "))
        print(f"Result: {height_feet}feet is {feet_to_meters(height_feet)}meters")
    elif choice == 4:
        distance_m = float(input("Enter distance in miles: "))
        print(f"Result: {distance_m}miles is {miles_to_km(distance_m)}kilometers")
    elif choice == 5:
        volume_gallons = float(input("Enter volume in gallons: "))
        print(f"Result: {volume_gallons}gallons is {gallons_to_liters(volume_gallons)}liters")
    else:
        print("Your choice is invalid. Please enter a number between 0 and 5")
