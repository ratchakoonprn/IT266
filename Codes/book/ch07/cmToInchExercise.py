length = float(input('Enter the length (cm): '))
if length < 0.0 :
    print('The entry is invalid')
else:
    inch = length / 2.54
    print('{:.2f} cm = {:.2f} inch'.format(length,inch))
