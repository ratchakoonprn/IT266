setA = {'Keyboard', 'Computer', 'Mouse', 'WiFi', 'Cable'}
setB = {'WiFi', 'Cable', 'Laptop', 'Touch Pen'}
#difference
diffSet = setA.difference(setB)
print('difference : ', diffSet)
#difference_update
setA.difference_update(setB)
print('difference update: ', setA)

