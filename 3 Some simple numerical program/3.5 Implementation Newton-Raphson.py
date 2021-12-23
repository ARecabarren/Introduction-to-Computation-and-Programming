#Comparing Newton-Raphson and Bisection search
#Find x such that x**2 - 24 is within epsilon of 0

def RootSqrt_BS(num):
    epsilon = 0.001
    numGuesses = 0
    low = 0.0
    high = max(1.0, num)
    ans = (high + low)/2.0
    while abs(ans**2 - num) >= epsilon:
        numGuesses += 1
        if ans**2 < num:
            low = ans
        else:
            high = ans
        ans = (high + low)/2.0

    print('Bisection Search: Square root of ' + str(num) + ' is about ' + str(ans) + '\n' +'Using ' +
          str(numGuesses) + ' guesses')
    
epsilon = 0.001
k = 24.0
guess = k/2.0
trys = 1
while abs(guess*guess - k) >= epsilon:
    guess = guess - (((guess**2) - k)/(2*guess))
    trys += 1
    


print('Newton-Rhapson: Square root of ' + str(k) + ' is about ' + str(guess) + '\n' +'Using ' +
      str(trys) + ' guesses')

RootSqrt_BS(24)

