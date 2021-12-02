score = int(input('Enter score: '))
time = int(input('Enter time: '))

if score > 1000 and time > 20:
    print('Game over')
if score > 1000 or time < 20:
    print('You win')