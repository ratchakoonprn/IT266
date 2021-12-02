a = 77
b = 55

# แบบปกติ
if a > b:
    print(f'{a} > {b}')

# แบบบรรทัดเดียว
if a > b: print(f'{a} > {b}')


# แบบปกติ
if a > b:
    print(f'{a} > {b}')
else:
    print(f'{a} <= {b}')

# แบบบรรทัดเดียว
print(f'{a} > {b}') if a > b else print(f'{a} <= {b}')