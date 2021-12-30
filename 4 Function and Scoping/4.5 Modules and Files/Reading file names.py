## Reading file

nameHandle = open('kids','r')
print("Let's start reading the names" + '\n')
for line in nameHandle:
    print(line)
nameHandle.close()
