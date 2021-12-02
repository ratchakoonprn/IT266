from random import randint

randNum = randint(1,50)
guessNum = int(input('Enter the number between 1 and 50: '))

if randNum == guessNum:
    print('You got it!!')
else:
    print('Sorry, the number is ',randNum)