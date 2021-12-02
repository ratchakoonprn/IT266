numbers = [85, 44, 3, 22, 1, 32, 24, 49, 11, 26, 20, 0, 10]
result = filter (lambda x: x > 20, numbers)
print(list(result))

def result(x):
    return x > 20
lst = filter(result,numbers)
print(list(lst))