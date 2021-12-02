from checkOddEven import is_even
number = int(input('Enter number: '))
if is_even(number):
    print(f'{number} is even number')
else:
    print(f'{number} is not even number')
