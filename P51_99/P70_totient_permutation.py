""" Find the value of n for which phi(n) is a permutation of n and the ratio n/phi(n) is minimized. 
remembering that n / phi(n) = 1 / product of (1-1/p)
to minimize this ratio, we want to maximize product (1 - 1/p)
That is, minimize the number of prime factors, and we want the prime factors to be as large as possible.

if n is just one prime factor, phi(n) = n-1, which is never a permutation of n.
Also note that if n = p^k, then phi(n) cannot be a permutation of phi(n).
That is because phi(p^k) = p^(k-1) * (p - 1)
n - phi(n) = p^k - (p^k - p) = p, which is never congruent to 0 mod 9. (which is a condition for two numbers to be permutations of each other)
Assume n has two different prime factors: n = p1 * p2

we want n and phi(n) to be permutations of each other. That means n-phi(n) = 0 mod 9
phi(n) = phi(p1) * phi(p2) = (p1-1)*(p2-1) = p1*p2 - p1 - p2 + 1
n - phi(n) = p1 + p2 - 1
so we want p1 + p2 = 1 mod 9

""" 

from math import isqrt
from math_utils import primes_less_than

lim = int(1e7)
primes = primes_less_than( 10 * isqrt(lim) )


result = 0
r = 2 # value we are trying to maximize 
for i in range(len(primes)):
    p1 = primes[i]
    if p1 * p1 > lim: break
    for j in range(i+1, len(primes)):
        p2 = primes[j]
        if (p1 + p2) % 9 != 1: continue
        
        n = p1*p2
        if n > lim: break
        
        phi = n - p1 - p2 + 1
        if n / phi > r: continue
        if sorted(str(phi)) == sorted(str(n)):
            r = n / phi
            result = n

print(result)