""" How many elements are in the farey sequence F_n ? 
for denominator = 2, we have 1/2
for denominator = 3, we have 1/3, 2/3 -> phi(3)
for denominator = 4, we have 1/4, 3/4  -> phi(4), note that 2/4 is not counted because it equated to a lower 

thus, we want sum{i: 1=>n}(phi(i))

We note that for prime numbers phi(p) = p-1
for composite numbers, n = product{i}( p_i ^ a_i ), phi(n) = product{i}( p^(i-1) * (p-1) )
Thus, we can start by letting phi(n) be n for all numbers, and then every time we discover a unique prime factor p|n,
then we divide the value we had in phi(n) by p and multiply by (p-1)
"""
from math import isqrt

n = int(1e6)
phis = [i for i in range(n+1)] # initialize to fill in phi(n) for prime n
phis[0] = 0

for i in range(2, n+1):
    if phis[i] != i: continue # i is prime

    phis[i] = i-1
    for j in range(2*i, n+1, i):
        phis[j] = (phis[j] // i) * (i-1)
    
print(sum(phis) - 1) # -1 to excluded 1/1