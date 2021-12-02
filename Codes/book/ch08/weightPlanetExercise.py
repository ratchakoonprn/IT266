earthWeight = float(input('Enter your weight(kg): '))
planetGravity = {'Moon':1.622, 'Mercury':3.7, 'Venus': 8.87}
for planet,gravity in planetGravity.items():
    weight = (earthWeight / 9.81) * gravity
    print(f'Weight on the {planet} is {weight:.2f} kg')


