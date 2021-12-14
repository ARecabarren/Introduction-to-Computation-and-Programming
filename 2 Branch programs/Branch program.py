#Write a program that examines three variables—x, y, and z—and
#prints the largest odd number among them. If none of them are odd, it should
#print a message to that effect.

x = 6
y = 4
z = 1


if z > y and z > x:
    if z%2 != 0:
        print("z is the largest odd number")
elif y > z and y > x:
    if z%2 != 0:
        print("y is the largest odd number")
elif x%2 != 0:
    print("x is the largest number")
else:
    print("Larger number isn't odd")