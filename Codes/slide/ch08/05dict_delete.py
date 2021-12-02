# การลบข้อมูล
student = {'Name':'Jane', 'Nationality':'Chinese', 'Bdate':'15-05-2005'}
print(f'student: {student}\n')

student.pop('Bdate')
print(f"pop('Bdate'):\n{student}\n") 

student.popitem()
print(f"popitem():\n{student}\n") 

c_student = student.copy()
print(f"clear: {c_student.clear()}\n")