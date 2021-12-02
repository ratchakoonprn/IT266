def fizzbuzz(i):
    if (i % 3 == 0 and i % 5 == 0):
        return 'fb'
    elif (i % 3 == 0):
        return 'f'
    elif (i % 5 == 0):
        return 'b'
    else:
        return str(i)

correct = 0
incorrect = 0
score = 0

maxRound = int(input('จำนวนรอบสูงสุดที่ต้องการเล่น : '))

for i in range(1, maxRound + 1):
    answer = input(f'{i} : ').lower()

    if (answer == '0'):
        break
    if (answer == fizzbuzz(i)):
        correct += 1
        score += 10
    else:
        incorrect += 1
        score -= 20
        if incorrect >= 3:
            break

print(f'ตอบถูก {correct}')
print(f'ตอบผิด {incorrect}')
print(f'คะแนน {score}')