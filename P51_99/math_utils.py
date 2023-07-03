import numpy as np 
from math import sqrt, gcd, isqrt
import math
from collections import deque

def simple_sieve(n):
    """ return an array of booleans where element [i] is true if 'i' is prime. """
    is_prime_arr = np.ones(n, dtype=bool) # Array where index 'i' is True if i is prime
    is_prime_arr[0] = is_prime_arr[1] = False
    sqrt_n = math.floor( np.sqrt(n) )
    for p in range(2, sqrt_n + 1, 1):
        if (is_prime_arr[p]):
            is_prime_arr[p*p::p] = False
    return is_prime_arr


# Simple sieve
def primes_less_than(n):
    """ Return an array of primes less than n. """
    is_prime_arr = simple_sieve(n)
    return np.flatnonzero(is_prime_arr)



def is_prime(n):
    """ Miller-Rabin primality test """
    # determine what bases are necessary
    if n == 2  or n == 3: return True
    if n%2 == 0 or n%3 == 0: return False

    if n < 1373653: bases = [2,3]
    elif n < 25326001: bases = [2,3,5]
    elif n < 3215031751: bases = [2,3,5,7]
    elif n < 2152302898747: bases = [2,3,5,7,11]
    elif n < 2**64: bases = list(primes_less_than(38))
    else: bases = list(primes_less_than(100))

    for p in bases:
        if pow(p, n-1, n) != 1: return False # Fermat's test
        
        d = n - 1
        while d%2 == 0:
           d = d // 2
           t = pow(p, d, n)
           if t == n-1: break
           if t != 1: return False
    return True

def sum_of_divisors_array(n):
    """ Return array with sum of proper divisors for all numbers <= n. """
    sigma_arr = [1] * (n+1)
    for i in range(2, isqrt(n)+1): # start from 2, so we only count proper divisors
        for j in range(i*i, n+1, i):
            sigma_arr[j] += i
            if j != i*i: sigma_arr[j] += j // i
    return sigma_arr


def pythagorean_triples(lim = np.inf):
    """ Yields all primitive pythagorean triples below a limit using Barning Trees
   https://en.wikipedia.org/wiki/Tree_of_primitive_Pythagorean_triples
    """
    yield np.array([3,4,5])
    q = deque( [np.array( [3,4,5])] ) # queue of pythagorean triples that should split off to produce more triples
    A = np.array([[1,-2,2], [2,-1,2], [2,-2,3]])
    B = np.array([[1,2,2] , [2,1,2],  [2,2,3]] )
    C = np.array([[-1,2,2], [-2,1,2], [-2,2,3]])
    while q:
        pyth = q.popleft()
        for M in [A,B,C]:
            pyth2 = M@pyth
            if pyth2.sum() < lim:
                q.append(pyth2)
                yield pyth2


# Functions for generating coprime pairs and pythagorean triples
def gen_mn(M):
    f = 1 + sqrt(2)
    for m in range(2, int(sqrt(f * M)) + 1):
        n0_tmp = int(sqrt(max(1, m * m - M * 2)))
        n0 = n0_tmp + (1 if (m + n0_tmp) % 2 == 0 else 0)
        for n in range(n0, min(m, M / m + 1), 2):
            if gcd(m, n) == 1:
                yield m, n
def gen_ab(M):
    for m, n in gen_mn(M):
        a = 2 * m * n
        b = m * m - n * n
        if a < b:
            yield a, b
        else:
            yield b, a


def cf_sqrt(n):
    """ Return a list with the terms of the continue fraction of sqrt(n) """
    a0 = isqrt(n) # sqrt(n) = a0 + 1/x
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

def convergents(D):
    """ Yield convergents of the continued fraction of sqrt(D),  p_n / q_n """
    cf = cf_sqrt(D)
    p0, q0 = math.isqrt(D), 1
    p1, q1 = p0 * cf[0] + 1, cf[0]
    yield (p1, q1)
    i = 1
    while True:
        a = cf[i]
        p1,q1,    p0,q0 = a*p1+p0, a*q1+q0,    p1,q1
        yield (p1,q1)
        i = (i + 1)%len(cf)