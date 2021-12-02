str = 'Python Programming'
d_count = {}
for letter in str:
    d_count[letter] = d_count.get(letter, 0) + 1
print(d_count)
