hotdog = []
onion = input('Adding onion (Y/N): ')
mustard = input('Adding mustard (Y/N): ')
ketchup = input('Adding ketchup (Y/N): ')
if onion.upper() == 'Y':
    hotdog.append('onion')
if mustard.upper() == 'Y':
    hotdog.append('mustard')
if ketchup.upper() == 'Y':
    hotdog.append('ketchup')
#print item in list
for topping in hotdog:
    print(topping,' is added')