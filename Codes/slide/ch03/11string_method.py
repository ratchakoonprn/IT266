my_string = 'Hi, Python!'
# upper()
print('--upper--')
print(my_string.upper())
print('hi'.upper())
print(my_string[:2].upper())
print(my_string[4:10].upper())

# lower()
print('--lower--')
print(my_string.lower())
print(my_string[:2].lower())
print(my_string[4:10].lower())

# title()
print('--title--')
print(my_string.lower().title())
print('alan turing'.title())

# capitalize()
print('--capitalize--')
print(my_string.capitalize())
print('alan turing'.capitalize())

# index
print('--index--')
print(my_string.index('P'))
print(my_string.index('thon'))
print(my_string.index(' '))
#print(my_string.index('p'))

# count
print('--count--')
print(my_string.count('i'))
print(my_string.count('p'))
print(my_string.count('H'))
print(my_string.upper().count('H'))