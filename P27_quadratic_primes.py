# b must be prime, because n^2 + a*n + b = b when n = 0, and we need the result to be prime when n = 0
# for n = 1, p = 1 + a + b ->  (1+b) + a -> even + a. so 'a' must be odd?

import numpy as np
import math

def prime_bool_arr(n):
    """ return a list of primes less than n """
    is_prime_arr = np.ones(n, dtype=bool) # Array where index 'i' is True if i is prime
    is_prime_arr[0] = is_prime_arr[1] = False
    sqrt_n = math.floor( np.sqrt(n) )
    for p in range(2, sqrt_n + 1, 1):
        if (is_prime_arr[p]):
            is_prime_arr[p*p::p] = False
    return is_prime_arr


n_limit = 500  # assume the best polynomial will produce this many consecutive primes. Modify if necessary
max_a = 999
max_b = 1000
limit = n_limit**2 + max_a*n_limit + max_b
is_prime_arr = prime_bool_arr(limit) # array telling us if a number n is prime or not, up to the highest possible prime in this problem
primes = np.flatnonzero(is_prime_arr)

primes = primes[ primes <= max_b ]

max_n = 0
best_a = 0
best_b = 0
for b in primes:
    # if b is odd, a must be odd as well
    for a in range(-max_a, max_a + 1, 1):
        n = 1 # we know n=0 produces a prime, so skip it
        while is_prime_arr[ n**2 + a*n + b ]:
            n += 1
        if n > max_n:
            max_n = n
            best_a = a
            best_b = b

print(best_a * best_b)
