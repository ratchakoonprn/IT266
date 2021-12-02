d_number = {'num1': 451, 'num2': 97.5, 'num3': -20}
# first result
print('First Method: ', sum(d_number.values()))
# second result
sum = 0
for key in d_number:
    sum = sum + d_number[key]
print('Second Method: ',sum)
