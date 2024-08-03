# Creating a BMI calculator
# Get the user's weight and height
weight = float(input("What is your weight in kg? "))
height = float(input("What is your height in meters? "))

# Calculate the BMI
BMI = weight / (height ** 2)

# Print the BMI
print("Your BMI is", round(BMI, 2))

# Determine the BMI category
if BMI < 18.5:
    print("You are underweight")
elif 18.5 <= BMI <= 24.9:
    print("You are normal")
elif 25 <= BMI <= 29.9:
    print("You are overweight")
elif 30 <= BMI <= 35:
    print("You are obese")
elif BMI > 35:
    print("You are severely obese")