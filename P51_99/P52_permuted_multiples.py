"""
Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.

Ideas: all those multiples must have the same number of digits. If the most significant digit is '2' or above, then 6x will have one more digit.
Therefore, the first digit must be '1'.


"""

from itertools import count

def P52():
    for d in count(2): # d is the number of digits
        for i in range(10**(d-1), 10**d):
            if all( [sorted(str(k*i)) == sorted(str(i)) for k in [6,5,4,3,2] ] ):
                print(i)
                return i


P52()
