from random import *
fund = 50
while (fund > 0 and fund <= 100):
    coin = randint(0, 1)
    guess = int(input('Enter your guess (Head: 1, Tail: 0): '))
    if coin == guess:
        fund +=10
        print('fund = ',fund)
    else:
        fund -=20
        print('fund = ', fund)
