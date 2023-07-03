""" Maximize n / phi(n) 

Starting with the formula: phi(n) = n * product of (1 - 1/p_i) for all unique prime factors of n
then n / phi(n) = 1 / product of (1-1/p_i)
Thus, we want to find a number which minimizes the product of (1-1/p_i).
This number gets smaller the more unique prime factors there are.
Also, we only want the smallest prime factors because qn/phi(qn) > n/phi(n)
so keep multiplying prime factors until we reach the limit.
"""

from math_utils import primes_less_than

lim = int(1e6)
primes = primes_less_than(lim)
n = 1
for p in primes:
    n = n * p
    if n > lim:
        n = n // p
        break

print(n)