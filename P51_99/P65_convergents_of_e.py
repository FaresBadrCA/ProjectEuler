6# From https://oeis.org/A003417
# Related topics: "Engel Expansion" and "Haros-Farey series"
from math import gcd

lim = 100
a0 = 2
cf = [1,2]
i, k = 0, 2
while len(cf) < lim - 1:
    if i%3 == 2:
        cf.append(2*k)
        k += 1
    else: 
        cf.append(1)
    i += 1

num, denom = 0, 1
for m in reversed(cf):
    num, denom = denom, m*denom + num # 1 / m*denom + num/denom
    g = gcd(num, denom)
    num = num // g
    denom = denom // g

result = a0*denom + num
print( sum( [int(c) for c in str(result)] ) )
