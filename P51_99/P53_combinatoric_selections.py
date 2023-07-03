"""
How many values of nCr are greater than one-million, for n between 1 and 100?

idea: for a given 'n', find the maximum value of nCr.

max r = n/2 if n is even, and (n-1)/2 if n is odd
then we decrement r until we drop below a million.
Then use the symmetry property of binomial coefficients: nCr = nC(n-r)

"""

import math

def P53():
    limit = int(1e6)
    n_limit = 100
    result_count = 0

    for n in range(n_limit, 1, -1):
        r = n // 2 # 'r' giving the highest value of nCr
        if math.comb(n, r) <= limit:
           print(result_count)
           return result_count

        if (n % 2) == 0:
            result_count += 1
        else:
            result_count += 2 # In odd case: (n-1)/2 and (n+1)/2 are above the limit

        while True:
            r -= 1 
            if math.comb(n, r) > limit:
                result_count += 2 # counting nCr and nC(n-r)
            else:
                break # Going to lower 'r' cannot go above the limit anymore




