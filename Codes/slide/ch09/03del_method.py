setA = {'Keyboard', 'Computer', 'Mouse', 'WiFi', 'Cable'}
setB = {'Wifi', 'Cable', 'Laptop', 'Touch Pen'}
setC = {'Keyboard', 'Mouse'}

# discard
print('--- discard ---')
setA.discard('Mobile')
print(f'Discard Mobile from setA = {setA}')

# pop
print('--- pop ---')
print(f'random pop(): {setB.pop()}')
print(f'setB after pop: {setB}')

# remove
print('--- remove ---')
setA.remove('Keyboard')
print(f'Remove Keyboard from setA: {setA}')

# clear
setB.clear()
print(f'set B after clear: {setB}')