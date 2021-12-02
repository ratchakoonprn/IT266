import os
dirname = os.path.dirname(__file__)
filename = dirname+'\data_motto.txt'
#print(filename)

f = open(filename,'r')
data = f.read()
print(data)
f.close()

# การเปิดไฟล์อีกวิธี

with open(filename,'r') as f:
    data = f.read()
    print(data)
    f.close()

