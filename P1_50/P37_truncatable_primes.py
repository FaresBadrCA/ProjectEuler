# Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

# start with a prime sieve and iterate forward. We do not have an upper bound so 

import numpy as np
import math

def prime_sieve(n):
    """ return a list of primes less than n """
    is_prime_arr = np.ones(n, dtype=bool) # Array where index 'i' is True if i is prime
    is_prime_arr[0] = is_prime_arr[1] = False
    sqrt_n = math.floor( np.sqrt(n) )
    for p in range(2, sqrt_n + 1, 1):
        if (is_prime_arr[p]):
            is_prime_arr[p*p::p] = False
    return is_prime_arr


def is_truncatable(p, is_prime_arr):
    r_trunc = p
    while r_trunc > 10:
        r_trunc = r_trunc // 10
        if not is_prime_arr[r_trunc]: return False

    n_digits = len(str(p))
    l_trunc = p
    while n_digits > 1:
        l_trunc = l_trunc % 10**(n_digits - 1)
        n_digits -= 1
        if not is_prime_arr[l_trunc]: return False

    return True

limit = 1000000
is_prime_arr = prime_sieve(limit)
primes = np.flatnonzero(is_prime_arr) 

result_list = [ p for p in primes if is_truncatable(p, is_prime_arr) and p > 10 ]

print(sum(result_list))
