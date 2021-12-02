x = int(input('Enter number: '))
y = int(input('Enter divider: '))
try:
  result = x/y
  print(f'{x} / {y} = {result:.2f}')
except:
    raise ZeroDivisionError("Divider can not be zero")
finally:
    print('Finished')
