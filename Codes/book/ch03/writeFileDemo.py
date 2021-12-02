f = open("data_motto.txt","a")
new_motto = input("Enter motto: ")
f.write(f'\n\n{new_motto}')
f.close()
