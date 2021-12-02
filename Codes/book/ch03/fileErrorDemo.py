try:
    f = open('myfile.txt')
    f.close()

except IOError:
    print('File not found. IOError occured.')
