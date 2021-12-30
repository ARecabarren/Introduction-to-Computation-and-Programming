# About files:
# the open() function creates the file 'kids' and indicates that we will write
# inside
nameHandle = open('kids', 'w')
for i in range(2):
    name = input('Enter name: ')
    nameHandle.write(name + '\n')
nameHandle.close()
