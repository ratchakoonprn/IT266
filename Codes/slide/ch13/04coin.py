# เกมทายเหรียญ
from random import *
fund = 50
play = 'y'
while (fund > 0 and fund <= 100) and (play == 'y'):
    coin = randint(0, 1)
    guess = int(input('\nหัวหรือก้อย(หัว: 1, ก้อย: 0): '))
    if coin == guess:
        fund +=10
        print('คุณทายถูก')
        print('คุณมีเงิน = ',fund)
    else:
        fund -=20
        print('คุณทายถูกผิด')
        print('คุณมีเงิน = ', fund)
    play = (input('คุณต้องการที่จะเล่นต่อหรือไม่ (y/n):')).lower()