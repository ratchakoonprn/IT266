setA = {'Keyboard', 'Computer', 'Mouse', 'WiFi', 'Cable'}
setB = {'Wifi', 'Cable', 'Laptop', 'Touch Pen'}
setC = {'Keyboard', 'Mouse'}

# isdisjoint
print('--- isdisjoint ---')
print('setA disjoints setB: ', setA.isdisjoint(setB))

# issubset
print('--- issubset ---')
print('setC is subset of setA: ', setC.issubset(setA))
print('setB is subset of setA: ', setB.issubset(setA))

# issuperset
print('--- issuperset ---')
print('setA is superset of setC: ', setA.issuperset(setC))
print('setB is superset of setC: ', setB.issuperset(setC))
