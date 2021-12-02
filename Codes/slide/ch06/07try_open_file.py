import os
dirname = os.path.dirname(__file__)
filename = dirname+'\myfile.txt'

try:
    f = open(filename)
    f.close()
 
except IOError:
    print('File not found. IOError occured.')