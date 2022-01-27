def biggest(dictionary):
    '''
    returns the key corresponding to the entry with the largest number of values associated with it. If there is more than
    one such entry, return any one of the matching keys.

    '''

    valuesList =[]
    for values in dictionary.values():
        valuesList.append(len(values))
    biggest = max(valuesList)

    for key in dictionary:
        if len(dictionary[key]) == biggest:
            return key

#Test Cases
# animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}
#
# animals['d'] = ['donkey']
# animals['d'].append('dog')
# animals['d'].append('dingo')
#
# print(biggest(animals))
# print(biggest({'b': [1, 7, 5, 4, 3, 18, 10, 0], 'a': []}))
