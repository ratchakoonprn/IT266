def leap_year(year):

  if ( year%4 == 0 and year%400 == 0 ) or ( year%4==0 and year%100 != 0):
    return True
  else:
    return False


  if ( year%4 != 0 ):
    return False
  else:
    if ( year%400 == 0 ):
      return True
    else:
      if ( year%100 == 0):
        return False
      else:
        return True


byear = int(input('ปี พ.ศ. ที่ต้องการตรวจสอบ :'))

year = byear - 543

print(f'พ.ศ. {byear} = ค.ศ. {year}')

if ( leap_year(year) == True ):
  print ('Leap year')
else:
  print ('Not leap year')
