#Assume s is a string of lower case characters.

#Write a program that counts up the number of vowels contained in the string s.
#Valid vowels are: 'a', 'e', 'i', 'o', and 'u'.
#For example, if s = 'azcbobobegghakl', your program should print:

#Number of vowels: 5

vowels = 'aeiouAEIOU'
s = 'azcbobobegghakl' #5 vowels
n = 'Alvaro' #3 vowels
c = 'n0tv0w3ls' #0 vowels
def countVowels(string):
    total = 0
    for letter in string:
        if letter in vowels:
            total += 1
    print(f'Number of vowels in {string}: {total}')

countVowels(s)
countVowels(n)
countVowels(c)
