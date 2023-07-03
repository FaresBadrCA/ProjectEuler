""" Note that after one iteration, the maximum value is 7*9^2 = 567 
Let s89 be the set of numbers <= 567 that reach 89.
For example, 2 is in s89.

How many numbers below 10^7 have the sum of their digits squared equal to 2?
Let f(n,k) be the number of ways n can be written as the sum of k squares.
The answer we seek is sum{ n in s89, 0<k<=7 }(f(n,k))

Note that f(n,k) = f(n-0^2, k-1) + f(n-1^2, k-1) + ... + f(n-9^2, k-1)
and f(n,0) = 0
and f(n,k) = 0 if n < 0
and f(0,0) = 1
"""

def c(n):
    return sum( int(x)**2 for x in str(n) )

dlim = 7 # limit in number of digits
lim1 = dlim * 9**2 # Maximum value after one iteration

s89 = set([89])
for i in range(1,lim1 + 1):
    L = []
    while True:
        if i in s89:
            s89.update(L)
            break
        if i == 1: break
        L.append(i)
        i = c(i)


d = { (0,0): 1 }
def f(n,k):
    """ Number of ways n can be written as a sum of k squares """
    if (n,k) in d: return d[(n,k)]

    if n < 0: return 0
    if k == 0: return 0
    
    s = 0
    for j in range(10):
        if k == 1 and j == 0: continue # The leftmost digit cannot be zero
        s += f(n-j**2, k-1)
    
    d[(n,k)] = s
    return s


print( sum( f(n,k) for n in s89 for k in range(1, dlim+1) ) )
