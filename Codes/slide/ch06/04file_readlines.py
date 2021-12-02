import os
dirname = os.path.dirname(__file__)
filename = dirname+'\data_motto.txt'

# อ่านข้อมูลทั้งหมด และเก็บไว้ในลิสต์
f = open(filename,'r')
data = f.readlines()
f.close()

print(f'list: {data}')

for line in data:
    print(line.strip()) # ใช้ strip เพื่อตัดช่องว่าง และ \n ออก