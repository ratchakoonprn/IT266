setA = {'Keyboard', 'Computer', 'Mouse', 'WiFi', 'Cable'}
setB = {'Wifi', 'Cable', 'Laptop', 'Touch Pen'}
setC = {'Keyboard', 'Mouse'}

# add
print('--- add ---')
setC.add('Monitor Stand')
print(f'setC = {setC}')

# copy
print('--- copy ---')
copy_setA = setA.copy()
print(f'copy_setA = {copy_setA}')

# update
print('--- update ---')
setC.update(setB)
print('Update setC: ', setC)