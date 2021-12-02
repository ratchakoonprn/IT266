setA = {'Keyboard', 'Computer', 'Mouse', 'WiFi', 'Cable'}
setB = {'WiFi', 'Cable', 'Laptop', 'Touch Pen'}
setC = {'Keyboard', 'Mouse'}
#copy
copySetA = setA.copy()
print('copySetA = ', copySetA)
#discard
setA.discard('Mobile')
print('Discard Mobile from setA = ', setA)
setA.discard('Cable')
print('Discard Cable from setA = ', setA)
#isdisjoint
print('setA disjoints setB: ', setA.isdisjoint(setB))
#issubset
print('setC is subset of setA: ', setC.issubset(setA))
print('setB is subset of setA: ', setB.issubset(setA))
#pop
print('random pop(): ', setB.pop())
print('setB after pop: ', setB)
#remove
setA.remove('Keyboard')
print('Remove Keyboard from setA: ', setA)
#update
setC.update(setB)
print('Update setC: ', setC)

