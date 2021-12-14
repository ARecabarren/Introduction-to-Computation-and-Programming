##Finger exercise: Write a program that asks the user to enter an integer and prints
##two integers, root and pwr, such that 0 < pwr < 6 and root**pwr is equal to the integer
##entered by the user. If no such pair of integers exists, it should print a message to that effect.

integer = int(input("Insert ann integer: "))
#root = 0
pwr = 1

while pwr < 6:
    root = 0
    while root < integer:
        if root**pwr == integer:
            break
        else:
            root+=1
    if root**pwr == integer:
            break
    pwr += 1

if root**pwr == integer:
            print("Founded pair; root =",root,"pwr =",pwr)
else:
    print("No such pair of integers exists")

