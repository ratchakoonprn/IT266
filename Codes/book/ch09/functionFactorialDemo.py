def factotial(n):
    if n == 1:
        return 1
    else:
        return n * factotial(n - 1)
n = 5
print(f'{n}! = {factotial(n)}')
