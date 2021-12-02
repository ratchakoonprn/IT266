studentPrice = 95
individualPrice = 159
familyPrice = 259
print('''
YouTube Premium Package
(1) Student
(2) Individual
(3) Family
''')
type = int(input('Enter package (1-3): '))
if type == 1:
    print (f'Student Package is {studentPrice} baht/month')
elif type == 2:
    print(f'Individual Package is {individualPrice} baht/month')
elif type == 3:
    print(f'Family Package is {familyPrice} baht/month')
else:
    print('You selected the wrong package')
