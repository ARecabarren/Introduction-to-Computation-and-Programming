from math import tan, pi

def polysum(n, s):
    surface = (0.25 * n * s * s) / tan(pi/n)
    bound_lenght = (n * s)**2

    return round(surface + bound_lenght, 4)

#test cases
print(pi)
print(polysum(60, 45))
print(polysum(6, 93))
print(polysum(7, 77))
print(polysum(5, 82))
