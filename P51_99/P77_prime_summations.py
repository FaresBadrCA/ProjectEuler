"""
Similar to coin counting problem #31

Comments of interest: 18 Aug 2005, 21:26

"""
from math_utils import simple_sieve, primes_less_than

lim = 100
is_prime = simple_sieve(lim)
primes = primes_less_than(100)

def partitions(n, m = 1):
    """ Return tuple of partitions of n starting at m """
    yield (n,)
    for i in range(m, n//2 + 1):
        for p in partitions(n-i, i):
            yield (i,) + p

def prime_partitions(n):
    if is_prime[n]: yield(n,)
    for i in range(2, n//2 + 1):
        if not is_prime[i]: continue
        for p in partitions(n-i, i):
            if all( [is_prime[k] for k in p] ): yield (i,) + p

# Alternative solution
N = 500
ways = [0] * (N+1)
ways[0] = 1;
for p in primes:
    for j in range(p, N+1, 1):
        ways[j] += ways[j - p]
        
import bisect
print( bisect.bisect_right(ways, 5000) )
