# How many circular primes are there below one million
import math
import numpy as np
from itertools import permutations

def prime_sieve(n):
    """ return a list of primes less than n """
    is_prime_arr = np.ones(n, dtype=bool) # Array where index 'i' is True if i is prime
    is_prime_arr[0] = is_prime_arr[1] = False
    sqrt_n = math.floor( np.sqrt(n) )
    for p in range(2, sqrt_n + 1, 1):
        if (is_prime_arr[p]):
            is_prime_arr[p*p::p] = False
    return is_prime_arr


# we want rotations not permutations
def is_circular(p, is_prime_arr):
    p_str = str(p)
    p_str = p_str[-1] + p_str[:-1]
    while p_str != str(p):
        if p_str[0] == '0': p_str = p_str[1:] # count '012' as '12'
        if is_prime_arr[ int(p_str) ] == False: return False
        p_str = p_str[-1] + p_str[:-1]
    return True

limit = 1000000
is_prime_arr = prime_sieve(limit)
primes = np.flatnonzero(is_prime_arr) 
result_list = [p for p in primes if is_circular(p, is_prime_arr)]

print(len(result_list))

