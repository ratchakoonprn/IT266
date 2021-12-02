n = 10

def power():
  n = 5
  print(f'local variable = {n}')
  print(f'{n} * {n} = {n*n}')

power()
print(f'global variable = {n}')