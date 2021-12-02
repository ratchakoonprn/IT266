setA = {'Keyboard', 'Computer', 'Mouse', 'WiFi', 'Cable'}
setB = {'WiFi', 'Cable', 'Laptop', 'Touch Pen'}
setC = {'Keyboard', 'Cable'}

# intersection
print('--- intersection ---')
setIntersec = setA.intersection(setB)
print('A intersection B: ', setIntersec)

# intersection_update
print('--- intersection_update ---')
setA.intersection_update(setB,setC)
print('A intersection_update B and C: ',setA)
