# กำหนดสมาชิก
countries = ("Thailand", "Australia", "China", "Singapore")
print(f'countries: {countries}')

# ใช้ฟังก์ชัน
f_tuple = tuple(["apple","cherry","kiwi"])
print(f'\nf_tuple: {f_tuple}')

# ทูเพิลมีสมาชิกเพียงตัวเดียว
a_tuple = ("apple",)
print(f'\na_tuple:{a_tuple}')
print(type(a_tuple))

# หากไม่ใส่ , จะมองว่าเป็น string
thistuple = ("apple")
print(f'\nthistuple: {thistuple}')
print(type(thistuple))