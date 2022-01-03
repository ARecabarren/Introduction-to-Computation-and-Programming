EtoF = {'bread':'pain', 'wine':'vin', 'with':'avec', 'I':'Je',
         'eat':'mange', 'drink':'bois', 'John':'Jean',
         'friends':'amis', 'and': 'et', 'of':'du','red':'rouge'}
FtoE = {'pain':'bread', 'vin':'wine', 'avec':'with', 'Je':'I',
         'mange':'eat', 'bois':'drink', 'Jean':'John',
         'amis':'friends', 'et':'and', 'du':'of', 'rouge':'red'}
dicts = {'English to French':EtoF, 'French to English':FtoE}

def translate_word(word, dictionary):
    if word in dictionary:
        return dictionary[word]
    elif word != '':
        return '"' + word + '"'
    return word

def translate(phrase, dicts, direction):
    UC_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    LC_letters = 'abcdefghijklmnopqrstuvwxyz'
    punctuation = '.,;:?'
    letters = UC_letters + LC_letters
    dictionary = dicts[direction]
    translation = ''
    word = ''
    for c in phrase:
        if c in letters:
            word = word + c
        elif word != '':
            if c in punctuation:
                c = c + ' '
            translation = (translation +
                        translate_word(word, dictionary) + c)
            word = ''
    return f'{translation} {translate_word(word, dictionary)}'

# print(translate('I drink good red wine, and eat bread.',
#                  dicts,'English to French'))
# print(translate('Je bois du vin rouge.',
#                  dicts, 'French to English'))

# print('bread' in EtoF)
# print(EtoF['bread'])

month_numbers = {'Jan':1, 'Feb':2, 'Mar':3, 'Apr':4, 'May':5,
                 1:'Jan', 2:'Feb', 3:'Mar', 4:'Apr', 5:'May'}
print(month_numbers.keys())
print(month_numbers.values())
print('May' in month_numbers)
# elements = []
# iter = 1
# for e in month_numbers:
#     elements.append(str(e))
#     print(f'For iteracion N{iter} list of elements is: {elements}')
#     iter +=1
