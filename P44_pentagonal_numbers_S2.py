"""
A second solution to the pentagonal numbers problem, provided by Nightingale (April 4, 2020) in the ProjectEuler forums.
We define four pentagonal numbers p_j and p_k, along with their sum: p_l and their difference p_i

A few mathematical derivations give us the rules to find p_i, which is what the question asks for:

[0] p(n) = n*(3*n - 1) / 2       Definition of the nth pentagonal number

[1] define: d = k - j
[2] j = (p_i - p_d) / 3d        derived by expanding (1) p_d and  (2) p_i = p_k - p_j using the pentagonal number formula and equating the two
[3] 3*d divides (P_i - P_d)     derived from [2]
[4] d congruent to i (mod 3)    derived from [3] with modulo arithmetic
[5] p_l = 2*p_j + p_i           derived from the definitions of p_l and p_i as the sum and difference of p_j and p_k

[6] p(n+1) - p(n) = 3n + 1      derived from [0]
[7] p(n+3) - p(n) = 

We do a forward search in p_i, and within that a forward search through 'd' until we find the first p_i meeting certain condition
[NOTE 1] By condition [3], we know to terminate the 'd' search when 3d > P_i - P_d
[NOTE 2] A number N is pentagonal is 1+24*N is a perfect square and if sqrt(1+24*N) is 5 mod 6. This is derived from the inverse of equation [0]

"""
import math

def is_pentagonal(n):
    """ A number N is pentagonal is 1+24*N is a perfect square and if sqrt(1+24*N) is 5 mod 6. This is derived from the inverse of the pentagional number equation """
    return math.sqrt(1 + 24 * n) % 6 == 5

def P44():
    i = 1
    while True: # Iterating through the pentagonal numbers one at a time. (p_i forward search)
        i += 1
        p_i = i * (3*i - 1) // 2
        
        d = i % 3  # Startaing value of 'd' is the smallest number > 0 and congruent to i (mode 3)
        if d == 0:
            d += 3

        p_d = d*(3*d - 1) // 2
        diff = p_i - p_d

        while 3*d <= diff: # By [3]: 3d divides (p_i - p_d), so 3d must be greater than (p_i - p_d)
            if diff % (3*d) == 0: # By [3]: 3d divides (p_i - p_d)
                j = diff // (3*d) # By [2]: j = (p_i - p_d) / 3d
                p_l = j*(3*j - 1) + p_i # By [5]:  p_l = 2*p_j + p_i
                if is_pentagonal(p_l): # p_l is the sum, which we require to be pentagonal. Once the sum and difference are confirmed as pentagonal, we're done searching
                    return p_i
            
            d += 3 # By [4]: d = i + 3K -> increment to next possible value of d
            p_d = d*(3*d - 1) // 2
            diff = p_i - p_d