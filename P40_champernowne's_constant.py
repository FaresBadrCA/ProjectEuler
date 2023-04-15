"""
Champernowne's constant, C10, is 0.1234567891011121314...

Question: find the 1st, 10th, 100th, 1000th, 10,000th, 100,000th and 1,000,000th digits of C10
"""
import math
# let's construct C10 as a string
C10 = '.' + ''.join([ str(i) for i in range(1, 500000) ])

math.prod( [ int( C10[10**i] ) for i in range(7)] )
