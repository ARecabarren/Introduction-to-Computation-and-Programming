# Write a procedure called oddTuples, which takes a tuple as input, and returns a new tuple as output, where every other
# element of the input tuple is copied, starting with the first one. So if test is the tuple ('I', 'am', 'a', 'test', 'tuple')
# , then evaluating oddTuples on this input would return the tuple ('I', 'a', 'tuple').

tuple = ('I','am','a','test','tuple')

def oddTuples(aTup):
    '''
    aTup: a tuple

    returns: tuple, every other element of aTup.
    '''
    oddTuples = ()
    for index in range(len(aTup)):
        if index%2 ==0:
            oddTuples += aTup[index:index+1]

    return oddTuples

# print(oddTuples((14,)))
# print(oddTuples((16, 18, 9, 18, 2, 1, 19, 7)))
