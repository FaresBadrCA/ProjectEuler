""" solving (b/n) * (b-1)/(n-1) = 1/2
2b^2 - 2b - n^2 + n = 0

There is a way to convert this to a pell equation. First, note that any number can be written as the product of two numbers. 
So let's substitute b = p*k, and n = p*j

2p^2k^2 - 2pk - p^2k^2 + pj = 0

now we can divide by p

2pk^2 - 2k - pj^2 + j = 0

At this point, we can still let p be anything we want, and (j,k) can adjust to keep the values of (b,n) anywhere on the number line
so we set p = 2k - j, and we substitute that in

2pk^2 - pj^2 - p = 0
dividing by p:      j^2 - 2k^2 = -1
This is the negative pell equation! and the first solution is (1,1)
so we can make an infinite number of solutions by taking odd powers of (1 + sqrt(2) )
(1+sqrt(2))*(1+sqrt(2)) = (3 + 2sqrt(2))

suppose(x,y) is a solution, then we get the next solution by:
(3+2sqrt(2))(x + y*sqrt(2)) = (3x + 4y,  3y + 2x)
""" 

lim = int(1e12)
j,k = 7,5
b,n = 15,21
while n < lim:
    j,k = 3*j + 4*k, 3*k + 2*j
    b = (2*k - j)*k
    n = (2*k - j)*j
