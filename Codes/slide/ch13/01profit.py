cost = 15000
sale1 = int(input('รายรับจาก ตุ๊ดตู่: '))
sale2 = int(input('รายรับจาก ติ๊ดตี่: '))
sale3 = int(input('รายรับจาก ตุ๊กติ๊ก: '))
sum = sale1+sale2+sale3
profit = sum - cost
donate = profit * 0.1
earn = (profit - donate) / 3
print(f'\nรายรับรวม: {sum:,.2f} บาท')
print(f'กำไรหลังจากหักต้นทุน: {profit:,.2f} บาท')
print(f'บริจาค: {donate:,.2f} บาท')
print(f'แต่ละคนได้รับเงินตอบแทน: {earn:,.2f} บาท')