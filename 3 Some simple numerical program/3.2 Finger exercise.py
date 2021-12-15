##Finger exercise: Let s be a string that contains a sequence of decimal numbers
##separated by commas, e.g., s = '1.23,2.4,3.123'. Write a program that prints the
##sum of the numbers in s.

s = '1.23,2.4,3.123'
total = 0
temp = ''
length = len(s)
for i in range(length):
    if s[i] != ',':
        temp += s[i]
    else:
        total += float(temp)
        temp = ''

total += float(temp)
print('Total',total)
    
