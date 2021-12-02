setA = {'Keyboard', 'Computer', 'Mouse', 'WiFi', 'Cable'}
setB = {'WiFi', 'Cable', 'Laptop', 'Touch Pen'}

#symmetric
symSet = setA.symmetric_difference(setB) # เก็บค่าใน set ตัวใหม่
print('symmetric : ', symSet)

#symmetric_update
setA.symmetric_difference_update(setB) # ปรับปรุงค่าลงในเซตเดิม
print('symmetric update: ', setA) 