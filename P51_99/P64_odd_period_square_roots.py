""" How many continued fractions have an odd period? 
"""
from math import sqrt, gcd

# Let 'standard form' be: (a*sqrt(n) + b) / c 
def cf_sqrt(n):
    a0 = int(sqrt(n)) # sqrt(n) = a0 + 1/x
    if a0*a0 == n: return []

    a, b, c = 1, a0, n - a0*a0 # x = (1/ (sqrt(n) - a0)) = (sqrt(n)+a0) / (n-a0^2) in standard form
    m = int( (a*sqrt(n) + b) / c)
    cf = [m] # (sqrt(n)+a0) / (n-a0^2) = m + 1/x
    while True:
        if a == 1 and c == 1: return cf # Reached sqrt(n) again so periodic from this point on
        #From previous loops, current term = a*sqrt(n)+b / c = m + 1/x 
        b = b - c*m # x = c / (a*sqrt(n) + b - c*m ), then redefine b => b - c*m
        d = n*a*a - b*b # x = (a*sqrt(n) - b)*c / (n*a^2 - b^2) 
        g = gcd(c,d) # simplify the fraction: c / (n*a^2 - b^2) 
        c, d = c//g, d//g
        a ,b, c = c*a, c*(-b), d # (a*sqrt(n) - b)*c / (n*a^2 - b^2) in standard form 
        m = int( (a*sqrt(n) + b) / c )
        cf.append(m)


N = 10_000
cnt = 0
for i in range(2, N+1):
    if len(cf_sqrt(i)) % 2 == 1: cnt += 1

print(cnt)