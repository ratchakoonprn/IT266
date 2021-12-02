def leap_year(year):
    if (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0):
        return 1
    else:
        return 0

byear = int(input('ปี พ.ศ. ที่ต้องการตรวจสอบ :'))
year = byear - 543
print(f'พ.ศ. {byear} = ค.ศ. {year}')
if leap_year(year):
    print('ปีอธิกสุรทิน (Leap Year)')
else:
    print('ไม่เป็น ปีอธิกสุรทิน (Not Leap Year)')
