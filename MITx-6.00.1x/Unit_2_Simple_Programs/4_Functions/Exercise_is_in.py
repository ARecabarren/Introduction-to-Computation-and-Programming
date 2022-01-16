
def isIn(char,aStr):
    '''
    Use an recursive implementation of bisection search to run through a txt
    checking if the center element is the letter
    ex. isIn('abcd','z') -> False
    ex. isIn('abcd','a') -> True
    '''

    #Base cases:
    if len(aStr) == 1 and char != aStr or aStr == '':
        return False
    #Succesfull case:
    elif char == aStr[len(aStr)//2]:
        return True
    #Guess lower than character:
    elif aStr[len(aStr)//2] > char:
        aStr = aStr[:len(aStr)//2]
        return isIn(char,aStr)
    else:
        aStr = aStr[len(aStr)//2 :]
        return isIn(char,aStr)



print(isIn('a',''))
print(isIn('r', 'ddddghkn'))
print(isIn('d', 'abhijjklnotuuuwxy'))
print(isIn('x', 'cdnruwy'))
print(isIn('w', 'cdfhijmuwz'))
