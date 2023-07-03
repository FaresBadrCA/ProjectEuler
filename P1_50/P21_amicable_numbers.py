"""
The problem defines d(n) as the sum of proper divisors, including 1 but excluding n.
Let's define D(n), which is the sum of proper divisors, excluding 1 but including n.

d(n) = D(n) + 1 - n

Conjecture: if two numbers have the same D(n), then they are an amicable pair

First, prime factorize n -> n = p1^e1 * p2^e2 ...
D(n) = p1 + p1*(D(n / p1)) + D( n / (p1^e1) )
"""

import numpy as np
import math
import itertools

def prime_sieve(n):
    """ return a list of primes less than n """
    is_prime_arr = np.ones(n, dtype=bool) # Array where index 'i' is True if i is prime
    is_prime_arr[0] = is_prime_arr[1] = False
    sqrt_n = math.floor( np.sqrt(n) )
    for p in range(2, sqrt_n + 1, 1):
        if (is_prime_arr[p]):
            is_prime_arr[p*p::p] = False
    return np.flatnonzero(is_prime_arr)


class DivisorAdder:
    """ Class for finding the sum of divisors of a number, denoted as d(n) """
    def __init__(self, limit):
        self.primes = prime_sieve( math.floor(np.sqrt(limit)) )
        self.D_cache = {0:0, 1:0} # Memoization: cache results of D(n). maps n : d(n)

    def sum_proper_divisors(self, n):
        """ d(n) = D(n) + 1 - n """
        if n == 0: return 0
        factors = self.prime_factorize(n)
        D = self.sum_divisors(n, factors)
        return D + 1 - n

    def sum_divisors(self, n, factors):
        """ 
        Input: n and its prime factorization as a list of tuples [(p1, e1), (p2,e2), ... ]
        return D(n) using D(n) = p1 + p1*(D(n / p1)) + D( n / (p1^e1) )   
        """
        if (n in self.D_cache): return self.D_cache[n]
        
        p1 = factors[0][0]
        e1 = factors[0][1]

        if e1 == 1:
            factor1 = [] # First factor will be removed
        else:
            factor1 = [(p1, e1 - 1)]

        D = p1 + p1 * self.sum_divisors(n // p1, factor1 + factors[1:]) + self.sum_divisors( n // (p1**e1), factors[1:] )
        self.D_cache[n] = D
        return D

    def prime_factorize(self, n:int):
        """ return list of tuples:  [ (p1, e1), (p2, e2), ... ], where n = p1^e1 * p2^e2 ...  
        The input list of primes must be sorted in ascending order, and only needs to go up to floor( sqrt(n) )
        """
        factors = []
        sqrt_n = math.floor( np.sqrt(n) )
        # assert primes is ascending and max(primes) >= sqrt_n
        for p in self.primes:
            if (n%p == 0):
                e = 0
                while (n%p == 0):
                    n = n // p
                    e += 1
                factors.append( (p,e) )
            if p > sqrt_n:
                break # If any number is left, it must be the last prime factor
        if n > 1:
            factors.append( (n, 1) )
        return factors

adder = DivisorAdder(limit = 10000)
for i in range(2, 10000):
    # print(i)
    x = adder.sum_proper_divisors(i)

# Find numbers in the dictionary with repeated 'D'
d_arr = [ D + 1 - n for n, D in adder.D_cache.items() ] # array with values of d(n)
result_list = []
for a, b in enumerate(d_arr):
    if b > len(d_arr) or a == b or a == 0 or b == 0:
        continue
    if d_arr[b] == a:
        result_list.append( (a,b) ) 
    
sum( [a+b for a,b in result_list]) // 2