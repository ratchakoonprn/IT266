f = open('D:\IT266\Codes\ch08\myfile.txt','a')
l= ['\nMy name is Ratchakoon\n','I like oranges']
f.writelines(l)
f.write(', grapes ')
f.write('and kiwi')
f.close()
