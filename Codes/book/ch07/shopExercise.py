items = int(input('Enter amount of items: '))
if items > 20:
    price = 45
elif items > 5:
    price = 50
else:
    price = 60

total = items * price
print('''You buy {} items with {:.2f} baht/item
The total price is {:,.2f} baht'''.format(items,price,total))
