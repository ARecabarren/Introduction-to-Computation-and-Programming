##Write a recursive Python function, given a non-negative integer N, to calculate and return the sum of its digits.
##
##Hint: Mod (%) by 10 gives you the rightmost digit (126 % 10 is 6), while doing integer division by 10 removes the rightmost digit (126 // 10 is 12).
##
##This function has to be recursive; you may not use loops!
##
##This function takes in one integer and returns one integer.

def sumDigits(N):
    '''
    N: a non-negative integer
    '''
    # Base cases:
    # One digit number
    if len(str(N)) == 1:
        return N
    else:
        return N % 10 + sumDigits(N // 10)

## Testing cases
##testDict = {}
##for key in range(1,100,3):
##    testDict[key] = sumDigits(key)
##
##print(testDict)
    
