import math

print(f'The value of e is {math.e}')
print(f"The value of e is {math.e:f}")
print(f'''The value of 
…   e is {math.e:.2f}'''
)
print(f'{1000000000:,}')

current = 60
highest = 500
print(f'{current} is {current/highest:.0%} of {highest}')
print(f'{16:d} {16:b} {16:x} {16:o}')

print(f'{16:+d} {32:-d}')
print(f'{"left":50}')
print(f'{"center":*^50}')