#Bref



def lastBalance(balance, annualInterestRate, fixedPayment):
    '''
    Takes parameters and iterates to know the balance at the end of 12 months

    balance: int, initicial Balance
    annualInterestRate: int or float, interest applied over unpaid balance after a year
    fixedPayment: int or float, mount reduced each month from the debt

    returns the final balance
    '''
    for i in range(12):
        temp = balance - fixedPayment
        balance = temp + temp * (annualInterestRate/12)
    return balance

def find_payment_BS(balance,annualInterestRate):
    founded = False
    lowerBound = balance/12.0
    upperBound = lastBalance(balance,annualInterestRate, 0)/12
    epsilon = 0.01
    midPoint = (upperBound + lowerBound)/2
    while not founded:
        testedBalance = lastBalance(balance, annualInterestRate, midPoint)
        if testedBalance > epsilon:
            lowerBound = midPoint
        elif testedBalance < -epsilon:
            upperBound = midPoint
        else:
            print('Lowest Payment:',round(midPoint,2))
            #print('Balance =',testedBalance)
            founded = True
        midPoint = (upperBound + lowerBound)/2

find_payment_BS(320000,0.2)
find_payment_BS(999999,0.18)
find_payment_BS(309101,0.18)
