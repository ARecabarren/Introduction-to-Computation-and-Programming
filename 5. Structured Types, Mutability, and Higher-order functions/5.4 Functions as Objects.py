def factR(n):
    """Assumes n an int > 0
        Returns n!
    """
    if n == 1:
        return 1
    else:
        return n*factR(n-1)

def fib(n):
    """Assumes n int >= 0
    Returns Fibonacci of n"""
    if n == 0 or n == 1:
        return 1
    else:
        print('Computing fib of ' + str(n))
        return fib(n-1) + fib(n-2)

def apply_to_each(L, f):
    """Assumes L is a list, f a function Mutates L
    by replacing each element, e, of L by f(e)"""
    for i in range(len(L)):
        L[i] = f(L[i])

L = [1, -2, 3.33]
print('L =', L)
print('Apply abs to each element of L.')
apply_to_each(L, abs)
print('L =', L)
print('Apply int to each element of', L)
apply_to_each(L, int)
print('L =', L)
print('Apply factorial to each element of', L)
apply_to_each(L, factR)
print('L =', L)
print('Apply fibonacci to each element of', L)
apply_to_each(L, fib)
print('L =', L)
