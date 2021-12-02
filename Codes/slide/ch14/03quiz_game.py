import os
dirname = os.path.dirname(__file__)
filename = dirname+'\quizgame.txt'

f = open(filename,"r")
nline = f.readlines()
f.close()
score = 0
print('มาทายตัวอักษรย่อของประเทศเหล่านี้กัน')
for line in nline:
  data = line.split(';')
  question = data[0]
  ans = data[1]
  uans = input(f'{question} : ')
  uans = uans.upper()
  if uans == ans:
    score +=1

print(f'Your score: {score}')