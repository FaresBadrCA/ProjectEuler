""" for Pell equation x^2 - D y^2 = 1, find D with the largest fundamental solution for D <= 1000

The solution for a pell equation must be a convergent of the continued fraction of sqrt(D)
Let sqrt(D) = [a0; a1, a2, a3 ... ak]
Let the kth convergent be: p_k / q_k
then solve q^2 - D*p^2 -> if it's 1, then we found the fundamental solution
then we find (p + q*sqrt(d))^2 = p^2 + d*q^2 + 2pq*sqrt(d) -> (p^2 + d*q^2, 2*pq) is the solution

The Farey sequence gives the convergents of a continued fraction  
https://www.math.uci.edu/~ndonalds/math180b/2pell.pdf
"""

import math
from math_utils import cf_sqrt

results = [ ( len(cf_sqrt(i)), i) for i in range(1001)]
sorted(results, reverse = True)

def solve_pell(D):
    """ Given the continued fraction for sqrt(D), find the minimal solution for x^2 - Dy^2 = 1 """
    sqrt_d = math.isqrt(D)
    if sqrt_d * sqrt_d == D: return (0,0)
    for x,y in convergents(D):
        if x**2 - D*y**2 == 1: return (x,y)

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

def p66(lim = 1000):
    result_x, result_D = 0, 0
    for D in range(2, lim + 1):
        x, y = solve_pell(D)
        if x > result_x: result_x, result_D = x, D
    return result_D

p66()