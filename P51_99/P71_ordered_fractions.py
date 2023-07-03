""" Use two properties of Farey sequences (F{n}):
    1) to generate a term between two terms, take the mediant.
    2) for F{n}, the sum of the denominators of two consecutive terms is less than n.

So we keep using property 1 to generate terms below 3/7 but getting closer to 3/7 until the sum of denominators exceeds the limit.

Better method: We use another property of Farey sequences: If we have two consecutive terms
x/y and h/k
then hy - kx = 1
We get an initial solution (y0, x0) by the extended euclidean algorithm.
Then we note that (y0 + rk, x0 + rh) is still a solution.
We choose r such that y0 - k < y0 + rk <= n
so r = (n-y0) // k

so we have x/y such that (y+h)>n and y <= n, so x/y is a term of the F{n}, and it is before h/k
""" 

from math import gcd

def extended_gcd(a, b):
    """ return gcd and bezout coefficients, (x,y) solving: ax + by = d, ensuring d is positive """
    r2, r = a, b
    s2, s = 1, 0
    t2, t = 0, 1
    while r != 0:
        q = r2 // r
        r2, r = r, r2 - q*r
        s2, s = s, s2 - q*s
        t2, t = t, t2 - q*t
    return (r2, s2, t2) if r2 >= 0 else (-r2, -s2, -t2)

n = int(1e6)
h,k = 3,7
g, y0, x0 = extended_gcd(h, -k)
r = (n - y0) // k
y = y0 + r*k
x = x0 + r*h
print(x)

