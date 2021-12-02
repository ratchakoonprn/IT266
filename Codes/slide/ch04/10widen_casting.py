# bool < int < float
print(float(1)) #int -> float
print(int(False)) #bool -> int
print(float(True)) #bool -> float

# auto casting
print(1/10.0) # int -> float
print(1+1.0) # int -> float
print(True+1) # bool -> int

# use function to cast
print(int(2.718)) #float -> int
print(bool(0)) #int -> bool
print(bool(1.0)) #float -> bool