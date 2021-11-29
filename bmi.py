
"""
Body Mass Index (BMI) is a measure of health on
weight. It can be calculated by taking your weight in
kilograms and dividing by the square of your height in
meters. The interpretation of BMI for people 16 years or
older is as follows:

BMI Interpretation

BMI < 18.5 Underweight

 18.5<= BMI < 25.0  --- Normal
25.0 <= BMI < 30.0  --- Overweight
30.0 <= BMI             Obese
"""
def calculation_body_mass_index():
    weight = float(input("Please enter your weight in kg: "))
    height = float(input("Please enter your height in meter: "))
    bmi = weight/(height**2)
    bmi = round(bmi,2)
    if bmi < 18.5:
        print("Your BMI is:", bmi, "You are Underweight, eat a little more!")
    elif (bmi >= 18.5 and bmi < 25.0):
        print("Your BMI is:", bmi, "Great you are Normal!")
    elif (bmi >= 25.0 and bmi < 30.0):
        print("Your BMI is:", bmi, "You are Overweight, start going to the gym!")
    else:
        print("Your BMI is:", bmi, "You are Obese, be very careful!")

if __name__ == '__main__':
    calculation_body_mass_index()
