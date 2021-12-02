hotdog = []
onion = input('Adding onion (Y/N): ')
mustard = input('Adding mustard (Y/N): ')
ketup = input('Adding ketup (Y/N): ')
if onion.upper() == 'Y':
    hotdog.append('onion')
if mustard.upper() == 'Y':
    hotdog.append('mustard')
if ketup.upper() == 'Y':
    hotdog.append('ketup')
#print item in list
for topping in hotdog:
    print(topping,' is added')
