import os
dirname = os.path.dirname(__file__)
filename = dirname+'\data_motto.txt'

# write ไปในไฟล์เดิม
"""f = open(filename,'a')
new_motto = input("Enter motto: ")
f.write(f'\n\n{new_motto}')
f.close()"""

# write ไปยังไฟล์ใหม่
newfile = dirname+'\new_motto.txt'
# เปิดไฟล์เดิม และเก็บข้อมูลไว้ใน data
f = open(filename,'r')
data = f.read()
f.close()
print(data)
n = open(newfile,'a+')
new_motto = input("Enter motto: ")
n.write(f'{data}\n{new_motto}')
n.close()