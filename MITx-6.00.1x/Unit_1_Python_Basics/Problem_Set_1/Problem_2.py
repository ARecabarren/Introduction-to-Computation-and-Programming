#Assume s is a string of lower case characters.

#Write a program that prints the number of times the string 'bob' occurs in s.
#For example, if s = 'azcbobobegghakl', then your program should print

#Number of times bob occurs is: 2

#s = 'azcbobobegghakl' #2 times
s = 'bobobobob' #4 times
#s = '' #empty

boundary = len(s) - 2
total = 0
for index in range(boundary):
    if index < (boundary):
        if s[index:index+3] == 'bob':
            total += 1
print('Number of times bob occurs is: ' + str(total))
