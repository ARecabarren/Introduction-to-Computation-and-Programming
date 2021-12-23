def factI(n):
    """Assumes n an int > 0
        Returns n!
    """
    result = 1
    while n > 1:
        result = n * result
        n = n-1
    return result

print(factI(4))
