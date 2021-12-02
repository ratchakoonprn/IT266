setA = {'Keyboard', 'Computer', 'Mouse', 'WiFi', 'Cable'}
setB = {'WiFi', 'Cable', 'Laptop', 'Touch Pen'}
setC = {'Keyboard', 'Cable'}
#intersection
setIntersec = setA.intersection(setB)
print('intersection: ', setIntersec)
#intersection_update
setA.intersection_update(setB,setC)
print('intersection_update: ',setA)
