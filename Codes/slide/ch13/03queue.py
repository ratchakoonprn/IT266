the_queue = []
n = 0
choice = 'Y'
while choice != 'X':
  choice = (input('จองคิว (Q) / เรียกคิว (N) / จบการทำงาน (X): ')).upper()
  if choice == 'Q':
    n += 1
    name = input('ชื่อลูกค้า: ')
    q = 'A'+ str(n)
    en_q = q +'-' + name
    the_queue.append(en_q)
    print(en_q)
    print(f'queue:{the_queue}')
  elif choice == 'N':
    de_q = the_queue.pop(0)
    print(de_q)
    print(f'queue:{the_queue}')
  else:
    print('***สิ้นสุดการทำงาน***')
    break