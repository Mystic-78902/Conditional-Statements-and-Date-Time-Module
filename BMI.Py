Height = float(input("enter your height in cm: "))
Weight = float(input("enter your weight in kg: "))

BMI = Weight / (Height/100)**2

print("Your BMI is", BMI)

if BMI <= 18.4:
    print("you are underweight")

elif BMI <= 24.9:
    print("you are healthy")

elif BMI <= 29.9:
    print("you are overweight")

elif BMI <= 34.9:
    print("you are severely over weight")

elif BMI <= 39.9:
    print("you are Obese")
else:
    print("you are severely obese")