def factR(n):
    """Assumes n an int > 0
        Returns n!
    """
    if n == 1:
        return 1
    else:
        return n*factR(n-1)

print(factR(4))
