import math

print('{} is a lucky number.'.format(13))

b = 9
c = 7
print('{} is greater than {}.'.format(b, c))
print('{1} is less than {0}.'.format(b, c))
print('{seven} is less than {nine}.'.format(nine=b, seven=c))
print('{1} {0} was born in {year}.'.format('Turing','Alan', year=1912))

# ทศนิยม
pi = math.pi
print('{:f}'.format(pi))
print('{:.2f}'.format(pi))
print('{:.8f}'.format(pi))

# หลักของตัวเลข
print('{:,}'.format(1000000000))
print('{:_}'.format(1000000000))

# เปอร์เซ็นต์
current = 60
highest = 500
print('{} is {:.0%} of {}'.format(current, current/highest, highest))

price = 8.89
total = 500
print('{} is {:.2%} of {}'.format(price, price/total, total))

# เลขฐาน 
# d ฐาน10 (decimal)
# b ฐาน2 (binary)
# x ฐาน16 (heximal)
# o ฐาน8 (octal)
print('{0:d} {0:b} {0:x} {0:o}'.format(16))
print('{0:d} {0:b} {1:x} {1:o}'.format(32,128))

# แสดงจำนวนบวก จำนวนลบ
print('{0:+d} {1:-d}'.format(16,-32))
print('{0:f} {1:f}'.format(16,-32))
print('{0:-x} {1:-x}'.format(16,-32))

#จัดชิดซ้าย ชิดขวา กึ่งกลาง
print('{:50}'.format('left'))
print('{:<50}'.format('left'))
print('{:>50}'.format('right'))
print('{:^50}'.format('center'))


print('{:!<50}'.format('left'))
print('{:>50}'.format('right'))
print('{:*^50}'.format('center'))