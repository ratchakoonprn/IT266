f = open("data_motto.txt","r")
data = f.readlines()
f.close()
print(f'list: {data}')
for line in data:
  print(line)
