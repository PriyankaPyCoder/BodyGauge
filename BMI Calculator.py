# BodyGauge:A Python-Based BMI Calculator for health assessment

while True:
    try:
        weight = float(input("Enter your weight in kilograms: "))
        height_ft = float(input("Enter your height in feet: "))

        if weight <= 0 or height_ft <= 0:
            print("Enter only positive values.\n")
            continue

        height_m = height_ft * 0.3048
        bmi = weight / (height_m ** 2)

        if bmi < 18.5:
            category = "Underweight"
        elif bmi < 25:
            category = "Normal weight"
        elif bmi < 30:
            category = "Overweight"
        else:
            category = "Obesity"

        print("\n--- Results ---")
        print(f"Weight: {weight} kg")
        print(f"Height: {height_m:.2f} meters (converted from {height_ft} feet)")
        print(f"Your BMI is: {bmi:.2f}")
        print(f"Category: {category}")

    except ValueError:
        print("Invalid input! Please enter numbers only.\n")
        continue

    choice = input("\nDo you want to calculate BMI again? (y/n): ").lower()
    if choice != 'y':
        print("Thank you for using BMI Calculator.")
        break
