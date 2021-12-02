student = dict(Name='Jane', Nationality='Chinese', Bdate='15-05-2005', Gender='F')
student['Name']='Jessica'
print(student)
student.update({'Name' : 'Jasmine'})
print(student)
del student['Bdate']
print(student)


