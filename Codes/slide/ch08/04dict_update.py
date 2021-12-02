# การปรับปรุงข้อมูล
student = {'Name':'Jane', 'Nationality':'Chinese', 'Bdate':'15-05-2005'}
print(f'student: {student}\n')
print(f"fromkeys:\n{dict.fromkeys(student,'allset')}\n") 

x=student.setdefault('Gender','M')
print(f"setdefault('Gender','M'):\n{student}\n") 

student.update({'Gender':'F'})
print(f"update():\n{student}\n") 