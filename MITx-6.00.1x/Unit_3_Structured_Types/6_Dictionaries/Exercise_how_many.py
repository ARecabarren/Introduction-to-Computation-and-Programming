def how_many(dict):
    '''
    dict : dictionary with list associated to the keys

    returns the number of values associated with a dictionary
    '''
    total = 0
    for key in dict:
        total += len(dict[key])
    return total


# Test case
# animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}
# animals['d'] = ['donkey']
# animals['d'].append('dog')
# animals['d'].append('dingo')
# print(how_many(animals))
