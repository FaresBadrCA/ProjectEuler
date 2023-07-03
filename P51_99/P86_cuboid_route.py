""" 
find the lowest value of M such that among all cuboids of size <= MxMxM, 
the shortest path from corner to corner is an integer.

shortest path = sqrt( (a+b)^2 + c^2 )

idea: get all pythagorean triples (a,b,c), with a<b<c
every 2-partition of a, a = a1+a2, results in a cuboid (a1,a2,b) which has shortest path 'c'
2-partitions of b into b1+b2 also results in cuboids (a,b1,b2) which have shortest path 'c'
"""

from math import sqrt
import numpy as np
from collections import deque

# results2 = []
# for a in range(1, max_m + 1):
#     for b in range(a, max_m + 1):
#         for c in range(b, max_m + 1):
#             p1 = sqrt( (a+b)**2 + c**2 )
#             if p1.is_integer():
#                 results2.append((a,b,c))

def pythagorean_triples(lim = np.inf):
    """ Yields all primitive pythagorean triples (a,b,c) where a <= lim
   https://en.wikipedia.org/wiki/Tree_of_primitive_Pythagorean_triples
    """
    yield np.array([3,4,5], dtype = np.int64)
    q = deque( [np.array( [3,4,5])] ) # queue of pythagorean triples that should split off to produce more triples
    A = np.array([[1,-2,2], [2,-1,2], [2,-2,3]])
    B = np.array([[1,2,2] , [2,1,2],  [2,2,3]] )
    C = np.array([[-1,2,2], [-2,1,2], [-2,2,3]])
    while q:
        pyth = q.popleft()
        for M in [A,B,C]:
            pyth2 = M@pyth
            if min(pyth2) <= lim:
                q.append(pyth2)
                yield sorted(pyth2.tolist())

max_m = 1818
results = []
for t in pythagorean_triples(max_m):
    a,b,c = t
    while a <= max_m:
        n_partitions = 0
        
        if b <= max_m: # cuboids from partition of a (a1, a2, b)
            n_partitions += a//2


        n_partitions += max(0, (2*a - b + 2) // 2) # cuboids from partitions of b: (a, b1, b2), where b1,b2 <= a

        if n_partitions > 0:
            results.append((n_partitions, a,b))
        else:
            break # 2a-b+1 <= 0, multiplying 'a' and 'b' by k>1 will only make this term more negative 

        a += t[0]
        b += t[1] # Handle all pythagorean triples, not just primitive ones
        c += t[2]

print( sum([x[0] for x in results]) )

