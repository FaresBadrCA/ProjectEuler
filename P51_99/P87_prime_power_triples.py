from math_utils import primes_less_than
from math import sqrt

lim = int(5e7)
p_arr = primes_less_than( int(sqrt(lim)) )

p2_arr = [p**2 for p in p_arr if p**2 < lim]
p3_arr = [p**3 for p in p_arr if p**3 < lim]
p4_arr = [p**4 for p in p_arr if p**4 < lim]

results = set()
for p2 in p2_arr:
    for p3 in p3_arr:
        p23 = p2 + p3
        if p23 > lim: break
        for p4 in p4_arr:
            x = p23 + p4
            if x < lim: results.add(x)
            else: break


print(len(results))