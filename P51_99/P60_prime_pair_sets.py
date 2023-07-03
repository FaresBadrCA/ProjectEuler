# Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.

from itertools import combinations, product
from collections import defaultdict
from math_utils import primes_less_than, is_prime

lim = int(1e4)

primes = primes_less_than(lim)
pairs_list = [ (p1,p2) for p1,p2 in combinations(primes, 2) if is_prime( int(str(p1)+str(p2)) ) and is_prime( int(str(p2)+str(p1)) )]

d, next_d = defaultdict(set), defaultdict(set)
for p1,p2 in pairs_list:
    d[(p1,)].add(p2)
    d[(p2,)].add(p1)


for _ in range(3):
    for tup, p_set in d.items():
        for p1, p2 in combinations(p_set,2):
            if not is_prime(int(str(p1)+str(p2)) ) or not is_prime(int(str(p2)+str(p1))): continue
            p_list = list(tup) + [p1, p2]
            for p in p_list:
                next_d[ tuple([x for x in p_list if x != p]) ].add(p)
    d, next_d = next_d, defaultdict(set)


result_list = [ (comb[0] + (comb[1],)) for tup, p_set in d.items() for comb in product([tup], p_set)]
print(min( map(sum, result_list)))

