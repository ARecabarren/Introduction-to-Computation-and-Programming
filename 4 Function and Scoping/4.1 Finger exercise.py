#Finger exercise: Write a function isIn that accepts two strings as arguments and
#returns True if either string occurs anywhere in the other, and False otherwise.
#Hint: you might want to use the built-in str operation in.

'''

'''
def isIn(string1,string2):
    if string1 in string2 or string2 in string1:
        return True
    else:
        return False

string1= 'Alvaro y Camille están casados'
string2= 'Alvaro'

print('Testing isIn function with :' +'\n'+ string1 +'\n' + string2)
print(isIn(string1,string2))
