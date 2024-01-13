height = float(input("What's your height in meters? "))
weight = float(input("What's your weight in kilogram? "))

BMI = round(weight / (height * height), 2)

print("Your BMI is", (BMI))

if (BMI <= 18.5):
    print("The classification of your BMI is Underweight")
elif (BMI > 18.5) or (BMI <= 24.9):
    print("The classification of your BMI is Normal weight")
elif (BMI > 24.9) or (BMI <= 29.9):
    print("The classification of your BMI is Overweight")
elif (BMI >= 30):
    print("The classification of your BMI is Obesity")   