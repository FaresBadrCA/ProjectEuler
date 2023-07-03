""" 
Use the mediant property of farey sequences to generate new terms until we cannot generate anymore.
The optimal solution has something to do with mobius inversions that I don't understand at the moment.
"""

from math import gcd

def p73(a=1, b=3, c=1, d=2, lim=12_000):
    q = [(a,b,c,d)]
    count = 0
    while q:
        a,b,c,d = q.pop()
        a2, b2 = a+c, b+d
        g = gcd(a2,b2)
        a2, b2 = a2//g, b2//g
        if b2 <= lim:
            count += 1
            q.append( (a,b, a2,b2) )
            q.append( (a2,b2,c,d) )
    return count

p73()