# copy
print('----- copy -----')
a = ['Jame', 'Anna']
c = a.copy()
print(c)

# reverse
print('----- reverse -----')
a = ['Jame', 'Anna', 'Paul', 'Patrick', 'Mark']
print(a)
a.reverse()
print(a)

# sort
print('----- reverse ascending -----')
a = ['Jame', 'Anna', 'Paul', 'Patrick', 'Mark']
print(a)
a.sort()
print(a)
print('----- reverse descending -----')
a = ['Jame', 'Anna', 'Paul', 'Patrick', 'Mark']
a.sort(reverse=True)
print(a)

# count
print('----- count Anna -----')
a = ['Jame', 'Anna','Eric','Anna','Patrick']
print(a)
d = a.count("Anna")
print(f'#Anna = {d}')

# index
print('----- index banana -----')
a = ['Jame', 'Anna', 'apple', 'banana', 'cherry']
print(a)
f = a.index('banana')
print(f'index = {f}')

# del
print('----- delete list -----')
cars = ["toyota","honda","nisson","mazda"]
print(cars)
del cars
print(f'after delete = {cars}')