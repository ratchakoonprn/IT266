setA = {'Keyboard', 'Computer', 'Mouse', 'WiFi', 'Cable'}
setB = {'WiFi', 'Cable', 'Laptop', 'Touch Pen'}

#difference
diffSet = setA.difference(setB)# เก็บค่าใน set ตัวใหม่
print('difference (in A,  not in B): ', diffSet)

#difference_update
setA.difference_update(setB)# ปรับปรุงค่าลงในเซตเดิม
print('difference update (update setA, not in B): ', setA)