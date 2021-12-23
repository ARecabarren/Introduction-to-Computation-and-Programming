##Finger exercise: What would the code in Figure 3.4 do if the statement x = 25
##were replaced by x = -25?

x = -25
epsilon = 0.01
numGuesses = 0
low = 0.0
high = max(1.0, x)
ans = (high + low)/2.0
while abs(ans**2 - x) >= epsilon:
    print('low =', low, 'high =', high, 'ans =', ans)
    numGuesses += 1
    if ans**2 < x:
        low = ans
    else:
        high = ans
        ans = (high + low)/2.0
print('numGuesses =', numGuesses)
print(ans, 'is close to square root of', x)

##Answer :
##    It start to report at each step a lower number because the statement
##    if ans**2 < x it's always false, the new maximum of the interval is each time
##    lower, reducing new guesses and not giving an answer 
##    
