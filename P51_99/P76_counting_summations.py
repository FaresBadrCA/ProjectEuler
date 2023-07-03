# Use recurrence relation of partitions 
# For generating all partitions of n: https://jeromekelleher.net/category/combinatorics.html

# For evaluating the parition function, Use recurrent relation p(n) = sum( p(n - k(3k - 1)/2) )
# The sum above is for all k where |k| <= sqrt(24n +1) + 1 / 6

from math import sqrt

d = {0 : 1} # memoization of p(n), taking p(0) to be 1
n = 10
lim_n = -1 * int( (sqrt(24*n + 1) - 1) / 6 )
lim_p = int( (sqrt(24*n + 1) + 1) / 6 )

def f_part(n):
    if n == 0: return 1
    lim_n = -1 * int( (sqrt(24*n + 1) - 1) / 6 )
    lim_p = int( (sqrt(24*n + 1) + 1) / 6 )
    result = 0
    for k in range(lim_n, lim_p + 1):
        if k == 0: continue
        pent = n - k*(3*k-1)//2
        if k%2 == 0: neg_fac = -1
        else:        neg_fac = +1
        if pent in d:
            result += neg_fac * d[pent]
        else:
            d[pent] = f_part(pent)
            result += neg_fac * d[pent]
    return result

r = f_part(1000)
print(r - 1)