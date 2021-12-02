student = dict(Name='Jane', Nationality='Chinese', Bdate='15-05-2005', Gender='F')
#print value only
for v in student.values():
    print(v)
print('********')

#print key only
for k in student.keys():
    print(k)
print('--------')

#print key and value
for k,v in student.items():
    print(k,v)