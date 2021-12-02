import json
# อ่านไฟล์
file = open('data_restaurant.json')

# อ่านข้อมูลเข้ามาเก็บเป็นดิกชันนารี
data = json.load(file)

# วนลูปอ่าน json ใน list
print('Read List:')
for item in data:
  print(item)

print('\nRead Restaurant Name:')
for item in data:
  print(item['name'])

file.close()