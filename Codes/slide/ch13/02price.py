def discount(price, percent):
  return price * ((100 - percent)/100)

price = int(input('Enter price: '))
percent = int(input('Enter percent discount: '))
print(f'New price: {discount(price,percent)}')