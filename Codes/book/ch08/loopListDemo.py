employees = ['Anna','Jane','Eric','Dave']
for emp in employees:
    print(f'{emp}',end=' ')

new_list = [emp for emp in employees]
print('\nnew_list: ',new_list)