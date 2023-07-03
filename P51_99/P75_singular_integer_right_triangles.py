# how many perimeters between 1 and 1.5M allow integer right triangles
# idea: Use the pythagorean triples generating formula to make all right triangles with perimeter in the desired range
# 

import numpy as np
from math_utils import pythagorean_triples

lim = 1_500_000
P = np.zeros(lim+1)
for t in pythagorean_triples(lim+1):
    s = t.sum()
    P[s::s] += 1

print( np.count_nonzero(P == 1) )