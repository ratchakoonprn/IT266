import json

# ข้อมูลที่จะเขียนลงไฟล์
new_dict ={
    "id" : 4,
    "name" : "pizza hours",
    "type" : 'Coupon, Partner'
}

# อ่านไฟล์
file = open('data_restaurant.json','r+',encoding='utf-8')

# อ่านข้อมูลเข้ามาเก็บเป็นดิกชันนารี
data = json.load(file)

# เขียนข้อมูลเพิ่ม
data.append(new_dict)
file.seek(0)
json.dump(data,file)

file.close()