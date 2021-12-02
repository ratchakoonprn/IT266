dict_Employee = {'e503':'Jintana', 'e561':'Paitoon','e610':'Kamonwan'}
print('''
Employees:
503 -> {0[e503]}
560 -> {0[e561]}
610 -> {0[e610]}
'''.format(dict_Employee))
#useing ** notation
print('''
Employees:
503 -> {e503}
560 -> {e561}
610 -> {e610}
'''.format(**dict_Employee))

