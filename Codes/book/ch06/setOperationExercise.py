setPaul = {'Running','Swimming','Riding','Hockey'}
setBob = {'Tennis','Riding','Running','Boxing','Footbal'}
print('All sports: ', setPaul.union(setBob))
print('Paul and Bob like: ', setPaul.intersection(setBob))
print('Bob likes different from Paul: ', setBob.difference(setPaul))
print('Paul and Bob like differently: ', setPaul.symmetric_difference(setBob))

