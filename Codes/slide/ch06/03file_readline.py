import os
dirname = os.path.dirname(__file__)
filename = dirname+'\data_motto.txt'

# หากไม่ใช้ loop จะอ่านแค่เพียงบรรทัดแรกบรรทัดเดียว
f = open(filename,'r')
print(f.readline())
f.close()

# ใช้ loop เพื่อวนอ่านและพิมพ์ข้อมูลในแต่ละบรรทัด
f = open(filename,'r')
for line in f:
  print(line)
f.close()
