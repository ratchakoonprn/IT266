setEmployee = {'Anan','Apinya','Chayakorn','Suthi','Panawan'}
print('Is Janjira an employee?: ', 'Janjira' in setEmployee)
print('Is Panawan an employee?: ', 'Panawan' in setEmployee)
setEmployee.remove('Anan')
print('List of Employees: ')
for emp in setEmployee:
    print(emp)
