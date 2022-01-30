##Write a Python function that returns a list of keys in aDict that map to
##integer values that are unique (i.e. values appear exactly once in aDict). T
##he list of keys you return should be sorted in increasing order.
##(If aDict does not contain any unique values, you should return an empty list.)
##
##This function takes in a dictionary and returns a list.

def uniqueValues(aDict):
    '''
    aDict: a dictionary
    '''
    # Your code here
    keys_List = aDict.keys()
    uniqueValuesKeys = []
    for key in keys_List:
        count = 0
        for value in aDict.values():
            if value == aDict[key]:
                count += 1
        if count == 1:
            uniqueValuesKeys.append(key)

    return sorted(uniqueValuesKeys)

#Some test cases
##print(uniqueValues({1: 1}))
##print(uniqueValues({1: 1, 2: 1, 3: 3}))
##print(uniqueValues({2: 2, 3: 3, 4: 4}))
