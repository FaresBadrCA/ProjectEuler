""" find bases and exponents, (b,e) such that b^e has e digits
numbers with e digits are in the range:  10^(e-1) <= x < 10^e
10^(e-1) <= b^e < 10^e
e-1 <= e * log(b) < e
(e-1)/e <= log(b) < 1

#1: b < 10, gives an upper bound on b
#2: (e-1)/e <= log(b) gives a lower bound on b
""" 
from math import log

cnt = 0
b,e = 1,1
while True:
    lbound = 10**((e-1)/e)
    if lbound > 9: break # base greater than 9 but less than 10. No options left. 

    for b in range(int(lbound), 10):
        digits = int( e * log(b, 10) ) + 1
        if digits == e: 
            cnt += 1
        elif digits > e: break
    e += 1

print(cnt)