
def lastBalance(balance, annualInterestRate, fixedPayment):
    for i in range(12):
        temp = balance - fixedPayment
        balance = temp + temp * (annualInterestRate/12)
    return balance

def find_payment(balance,annualInterestRate):
    founded = False
    step = 10
    while not founded:
        if lastBalance(balance, annualInterestRate, step) <0:
            print('Lowest Payment:',step)
            founded = True
        else:
            step += 10

# Test Cases
# find_payment(3329,0.2)
# find_payment(3926,0.2)
# find_payment(4773,0.2)
# find_payment(721,0.2)
