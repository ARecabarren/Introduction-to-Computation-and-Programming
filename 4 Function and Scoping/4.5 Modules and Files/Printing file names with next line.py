names = open('kids','w')
names.write('Alvaro\n')
names.write('Camille\n')
names.close()


names = open('kids','r')
for name in names:
    print(name[:-1])

