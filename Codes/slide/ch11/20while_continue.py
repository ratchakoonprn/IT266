nums = [1,2,3,4,5,6,7,8,9,10]
x = 0
while (x < 10):
    if nums[x] == 3:
        x = x+1
        continue
    print(nums[x])
    x = x+1