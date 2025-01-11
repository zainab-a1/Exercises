def calculate_bmi(weight, height):
    calculation = weight / (height * height)
    return calculation

def total(weight, height):
    calculate= calculate_bmi(weight,height)
    if calculate <= 18:
        print("Underweight")
    elif calculate > 18.5 and calculate <= 25:
        print("Norm")
    else:
        print("Overweight")