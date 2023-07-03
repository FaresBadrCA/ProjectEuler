from math import sqrt

def num_minterms(n, p, s, n_factors = 0, min_factor = 2):
    """ Return count of values of k (below limit) for which n is a minimum sum-product number 
    n: sum-product number candidate
    p: product remaining after some factors have been taken out of n
    s: sum remaining after those factors were subtracted from n
    n_factors: count of factors taken out of n
    min_factor: lower bound on numbers that can divide p
    """
    k = n_factors + 1 + s - p # factors taken out of n, then n itself, then #ones needed to make sum and product equal
    result = 0 # count of values of k below limit whose minimum sum-product is n
    if k <= LIMIT and n_factors > 0 and (d[k] == 0 or d[k] > n): 
        d[k] = n # new minimum product-sum number found!
        result += 1

    for i in range(min_factor, int(sqrt(n))+1):
        if p % i == 0:
            result += num_minterms(n, p // i, s - i, n_factors + 1, i)

    return result

LIMIT = 12000
d = [0]*(LIMIT+1) # d[k] is the lowest sum-product number for a given length, k. 0 if none found yet. 
n = 2 # n is a product-sum candidate
remaining = LIMIT - 1 # count of sum-product numbers we need to find. 2->lim
while remaining:
    remaining -= num_minterms(n,n,n)
    n += 1

print(sum(set(d)))