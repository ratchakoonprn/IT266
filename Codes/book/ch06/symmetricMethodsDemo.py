setA = {'Keyboard', 'Computer', 'Mouse', 'WiFi', 'Cable'}
setB = {'WiFi', 'Cable', 'Laptop', 'Touch Pen'}
#symmetric
symSet = setA.symmetric_difference(setB)
print('symmetric : ', symSet)
#symmetric_update
setA.symmetric_difference_update(setB)
print('symmetric update: ', setA)

