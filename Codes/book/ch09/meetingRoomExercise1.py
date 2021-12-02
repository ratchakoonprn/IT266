# 2. ตรวจสอบว่าในวันที่กำหนด มีเวลาใดว่างบ้าง
# รับอาร์กิวเมนต์ didx คือ day index
def get_time_available (didx):
  t = [idx for idx,val in enumerate(room[didx]) if val == None ]
  return t

# 2. แสดงเวลาที่ห้องประชุมว่าง
# พิมพ์ช่วงเวลาที่ว่าง
# รับอาร์กิวเมนต์ tdic คือ คำอธิบาย dictionary ของเวลา และ tlis คือ list ของเวลาที่ว่าง
def print_time(tdic,tlist):
  print('เวลาที่ว่างคือ:')
  [print(tdic[idx]) for idx in tlist]

# 2. รับเวลา และ ชื่อผู้จอง
def get_user():
  tbooking = int(input('กรุณาเลือกเวลาที่ต้องการจองห้องประชุม: '))
  tidx = tbooking - 1
  user = input('กรอกชื่อผู้จอง: ')
  return tidx,user

# 3. บันทึกการจองห้องประชุม
# รับอาร์กิวเมนต์
# didx คือ index ของวันที่ต้องการจอง
# tidx คือ index ของช่วงเวลาที่ต้องการจอง
# username คือ ชื่อผู้จอง
def set_booking(didx,tidx,user):
  room[didx][tidx] = user
  print('**Booking Done**')

# สร้างตารางจองห้องประชุม List
room = [['Jane','Jeff','Paul','John'],
        [None,'Jeff','Paul',None],
        [None,'Chris',None,'John'],
        [None,None,None,'Emily'],
        ['Jane',None,'Anna',None]]
# สร้างดิกชันนารีช่วงเวลา
time = {0:'เวลา 09:00 - 11:00 กด 1',
        1:'เวลา 11:00 - 13:00 กด 2',
        2:'เวลา 13:00 - 15:00 กด 3',
        3:'เวลา 15:00 - 17:00 กด 4'}

dayName = ['จันทร์','อังคาร','พุธ','พฤหัส','ศุกร์']

#1. รับวันที่ต้องการจองห้องประชุมในแต่ละสัปดาห์จากผู้ใช้
day = int(input('วันที่ต้องการจองห้องประชุม (1 - 5): '))
didx = day - 1

available = get_time_available(didx)
if available != []:
  print_time(time,available)
  tidx,user = get_user()
  set_booking(didx,tidx,user)
  print('\nตารางห้องประชุม:')
  print(room)
else:
  print(f'ไม่มีห้องประชุมว่างในวัน{dayName[didx]}')

print('*******')