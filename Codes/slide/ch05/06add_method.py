# append
print('----- append -----')
a = ['Jame', 'Anna']
a.append('Mike')
print(a)

a = ['Jame', 'Anna']
b = ['Mike', 'April']
a.append(b)
print(a)

# extend
print('----- extend -----')
a = ['Jame', 'Anna']
e = ['apple', 'banana', 'cherry']
a.extend(e)
print(a)

# insert
print('----- insert -----')
a = ['Jame', 'Anna']
a.insert(0,'Hi')
print(a)

# clear
print('----- clear -----')
b = ['Mike', 'April']
b.clear()
print(b)