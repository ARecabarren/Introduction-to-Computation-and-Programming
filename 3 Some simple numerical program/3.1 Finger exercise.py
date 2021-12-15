##Finger exercise: Write a program that asks the user to enter an integer and prints
##two integers, root and pwr, such that 0 < pwr < 6 and root**pwr is equal to the integer
##entered by the user. If no such pair of integers exists, it should print a message to that effect.

integer = int(input("Insert an integer: "))
root = 0
pwr = 1

found = False
if integer < 0:
    isNeg = True
else:
    isNeg = False



while pwr < 6:
    root = 0
    while abs(root) <= abs(integer):
        if abs(root**pwr) > abs(integer):
            break
        if root**pwr == integer:
            found = True
            print(str(root) + "**" + str(pwr) + " = " + str(integer))
        if isNeg:
            root -= 1
        else:
            root+=1
    pwr += 1

if not found:
            print("No such pair of integers exists")
    

