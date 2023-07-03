""" Find [a,b,c,d] which can form all numbers from 1 to n by concatenating them with operators (+,-,*,/) in any order """
from itertools import combinations

def cat2(a,b):
    return set([a+b, a-b, b-a, a*b, a/b, b/a])

memo = {} 

def cat(t):
    """ Given a sorted tuple, t, return the set, R, of any combinations of (+,-,*,/) on the elements of t """
    if t in memo: return memo[t]

    if len(t) == 2:
        R = cat2(t[0], t[1])
        memo[t] = R
        return R

    R = set()
    for a in t:
        R2 = cat( tuple(x for x in t if x != a) )
        for b in R2:
            R.update([a+b, a-b, b-a, a*b])
            if b != 0: R.add(a/b)
            if a != 0: R.add(b/a)

    memo[t] = R
    return R

 
best_c, best_v = 0, 0
for c in combinations( range(1,10), 4 ):
    c = tuple(sorted(c))
    result = sorted( int(a) for a in cat(c) if float(a).is_integer() and a >= 1 )

    i = 1
    for n in result:
        if n != i: break
        i += 1

    i -= 1
    if i > best_v: 
        best_v = i
        best_c = c
        
print(best_c)
