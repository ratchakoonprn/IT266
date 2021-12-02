student = {'Name':'Jane', 'Nationality':'Chinese', 'Bdate':'15-05-2005'}
c_student = student.copy()
print(c_student) #{'Name': 'Jane', 'Nationality': 'Chinese', 'Bdate': '15-05-2005'}
print(dict.fromkeys(c_student,'allset')) #{'Name': 'allset', 'Nationality': 'allset', 'Bdate': 'allset'}
print(c_student.clear()) #None
print(student.get('Name')) #Jane
print(student.items()) #dict_items([('Name', 'Jane'), ('Nationality', 'Chinese'), ('Bdate', '15-05-2005')])
print(student.keys()) #dict_keys(['Name', 'Nationality', 'Bdate'])
student.pop('Bdate')
print(student) #{'Name': 'Jane', 'Nationality': 'Chinese'}
student.popitem()
print(student) #{'Name': 'Jane'}
x=student.setdefault('Gender','M')
print(x) #M
student.update({'Gender':'F'})
print(student)  #{'Name': 'Jane', 'Gender': 'F'}
print(student.values()) #dict_values(['Jane', 'F'])

