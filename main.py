# Underweight: BMI < 18.5

# Normal weight: 18.5 ≤ BMI < 24.9

# Overweight: 25 ≤ BMI < 29.9

# Obesity: BMI ≥ 30


weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

BMI = weight / (height ** 2)
print("BMI:", BMI)
if BMI < 18.5:
    print("You are under weight.")
elif BMI >= 18.5 and BMI < 24.9:
    print("You are normal weight.")
elif BMI >= 25 and BMI < 29.9:
    print("You are over weight.")
elif BMI >= 30:
    print("You are obese.")

