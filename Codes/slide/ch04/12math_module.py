import math
pi = math.pi #3.141592653589793
e = math.e #2.718281828459045
inf = math.inf 
nan = math.nan #nan
#circle constant (2𝞹)
tau = math.tau #6.283185307179586 
print(pi)
print(e)
print(inf)
print(nan)
print(tau)

# ฟังก์ชันพื้นทำการปัดเศษทิ้งโดยการปัดลง
print(math.floor(pi))
# ฟังก์ชันเพดานทำการปัดเศษทิ้งโดยการปัดขึ้น
print(math.ceil(pi))

# แปลงมุม เปลี่ยน radians เป็น degrees
print(math.degrees(math.pi))
# แปลงมุม เปลี่ยน degrees เป็น radians
print(math.radians(180)) #𝞹
print(math.radians(90)) #𝞹/2

# sin, cos, tan
print(math.sin(math.pi))
print(math.cos(math.pi))
print(math.tan(math.pi))

# asin, acos, atan
print(math.acos(1))
print(math.asin(1))
print(math.atan(1))

# Exponential function
print(math.exp(1))
print(math.exp(10))
print(math.exp(50))

# Power
print(math.pow(2,2))
print(math.pow(2,7))
print(math.pow(3,-1))