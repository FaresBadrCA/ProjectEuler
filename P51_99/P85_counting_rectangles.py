""" For an mxn grid, let S(a,b) be the number of rectangles of size axb
Let T be the sum of S(a,b) for all a<m,b<n
We find T = (1/4) * (n^2 + n) * (m^2 + m)

Let B be the desired number of rectangles. 

then for every m from 1 to the square root of the bound, we can calulate the greatest n that results in T < B
and we calculate the n right above that, keeping track of which (m,n) combination resulted in the lowest |T-B|

The bound on m can be made much stricter (see 22 Jan 2023, 09:34): 
by noting that (m,n) is the same as (n,m), we only need to search where m < n
when m = n: T = m*(m+1)*m(m+1) < (m+1)^4
we want this less than 4*B
therefore, m < (4B)^(1/4)


"""

from math import sqrt

def P85(bound = 2*10**6):
    m0, n0 = 0,0
    lowest_diff = bound
    m_max = int( (4*bound)**0.25 )
    for m in range(1, m_max + 1):  
        m_term = m**2 + m
        n = (-1 + sqrt(1 + 16*bound/m_term  )) / 2
        n1 = int(n)
        t1 = n1*(n1+1)*m_term
        if bound - t1 < lowest_diff:
            lowest_diff, m0, n0 = bound - t1, m, n1

        n2 = n1 + 1
        t2 = n2*(n2+1)*m_term
        if t2 - bound < lowest_diff:
            lowest_diff, m0, n0 = t2 - bound, m, n2

    return m0, n0


a,b = P85()