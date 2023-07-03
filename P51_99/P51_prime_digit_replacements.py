"""
Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit, is part of an eight prime value family.

Iterate through primes with d digits. For each prime, p, identify all combinations of k digits that are identical.
For each combination, replace those k digits by '*'. Let that string be called r_str.

As we iterate through primes, for every combination of k identical digits, increment the count of the resulting r_str until we hit a count of '8'.
"""


from math_utils import primes_less_than

from itertools import combinations
from collections import defaultdict

def P51(d, k, limit = 8):
    """
   d: #digits in prime
   k: #digits to replace with identical digits
   limit: size of prime family we're looking for
    """
   
    r_str_count = defaultdict(int)  # map r_str to the number of times it was encountered 
    primes = primes_less_than(10**d)
    primes = primes[ primes > 10**(d-1) ] # Primes with d digits only

    for p in primes:
        digit_dict = defaultdict(list)
        for i,c in enumerate(str(p)):
            digit_dict[c].append(i)
        repeated_spots = [v for v in digit_dict.values() if len(v) >= k] # indices of digits repeated at least k times

        repeated_spot_comb = [] # List of tuples. Each tuple is a combination of k digits that are identical in 'p'
        for spot_list in repeated_spots: # Spot list can be of size greater than k 
            repeated_spot_comb.extend( combinations(spot_list, k) )

        for comb in repeated_spot_comb:
            r_str = ''.join( [ c if i  not in comb else '*' for i,c in enumerate(str(p))] ) # 56003 -> 56**3
            r_str_count[r_str] += 1

            if r_str_count[r_str] == limit:
                return r_str
    return None # No answer found


r_str = P51(6,3)