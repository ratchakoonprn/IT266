status = True
while status:
    height = float(input('Enter height (cm): '))
    weight = float(input('Enter weight (kg): '))
    bmi = weight / ((height/100)**2)
    if bmi < 18.5:
        text = 'Underweight'
    elif bmi < 24.9:
        text = 'Normal weight'
    elif bmi < 29.9:
        text = 'Overweight'
    else:
        text = 'Obese'
    print('BMI = {:.1f} -> {}'.format(bmi, text))
    choice = input('Do you want to calculate another BMI (Y/N): ').upper()
    if choice != 'Y':
        status = False
