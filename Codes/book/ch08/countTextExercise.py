text = 'This is Python loop'
count = 1
words=text.split()
for ch in text:
    if ch == ' ':
        count +=1
print(f'There are {count} words: {words}')
#text = 'There are ' + count + 'words ' + words

