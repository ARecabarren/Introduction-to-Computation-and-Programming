##Finger exercise: What would have to be changed to make the code in Figure 3.4
##work for finding an approximation to the cube root of both negative and positive
##numbers? (Hint: think about changing low to ensure that the answer lies within
##the region being searched.)

x = 27

if x < 0:           #We create a flag to indicate that we search the cube root for a negative number
    isNeg = True
else:
    isNeg = False
    
epsilon = 0.01
numGuesses = 0
                    # Then if the number is negative we want to redefine the range setting the x to the lower value
if isNeg:
    low = x
else:
    low = 0.0
                    # For this segment only rest to change the pwr 2 by 3
high = max(1.0, x)
ans = (high + low)/2.0
while abs(ans**3 - x) >= epsilon:
    print('low =', low, 'high =', high, 'ans =', ans)
    numGuesses += 1
    if ans**3 < x:
        low = ans
    else:
        high = ans
    ans = (high + low)/2.0
print('numGuesses =', numGuesses)
print(ans, 'is close to cube root of', x)
