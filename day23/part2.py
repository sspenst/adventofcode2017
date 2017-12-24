def is_prime(n):
    """ Implemented based on the GMP library source code """
    if n < 3 or n & 1 == 0:
        return n == 2

    d = 3
    r = 1

    while r != 0:
        q = n // d
        r = n - q * d
        if q < d:
            return True
        d += 2

    return False

"""
The provided input loops through the values b to c in increments of 17.
If the value has a pair of factors, h ends up being incremented.
"""

b = 108100
c = 125100
h = 0

for g in range(b, c + 1, 17):
    if is_prime(g) == False:
        h += 1

print(h)
