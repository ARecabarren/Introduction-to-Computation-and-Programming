# Apending to not overwrite the file

namesHandle = open('kids','a')
namesHandle.write('Remi\n')
namesHandle.write('Juliette\n')
namesHandle.close()

namesHandle = open('kids','r')
for name in namesHandle:
    print(name[:-1])
namesHandle.close()

#Notice that each time that we open this file, the names Remi and Juliette are
#added again
