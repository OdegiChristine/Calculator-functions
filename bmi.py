mass = float(input("Enter mass in kilograms: "))
height = float(input("Enter height in metres: "))

def body_mass_index(weight, h):
    n_bmi = weight/(pow(h,2))
    bmi = round(n_bmi,2)
    if bmi < 18.5 :
        print(f"Your BMI is {bmi}")
        print("You are underweight")

    elif (bmi >=18.5) and (bmi <=24.9):
        print(f"Your BMI is: {bmi}")
        print("You have normal weight")

    else:
        print("You are overweight")

    return bmi

result = body_mass_index(mass, height)
