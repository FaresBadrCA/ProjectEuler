"""
List all numbers that cannot be written as the sum of two abundant numbers
We know that they are less than 28123

basic idea: list all abundant numbers from 1 to 28123
make an array of size 28123 and mark sums of numbers as false

"""

import numpy as np
from P21_amicable_numbers import DivisorAdder

limit = 28123
adder = DivisorAdder(limit = limit)

sum_divisor_list = [ adder.sum_proper_divisors(i) for i in range(limit) ]

abundant_numbers = [ i for i,d in enumerate(sum_divisor_list) if d > i ]

# We have a list of numbers, we need to find numbers that CANNOT be written as a sum of two numbers from this list
not_sum_of_abundant = np.ones(limit, dtype = bool)
for a in abundant_numbers:
    for b in abundant_numbers:
        if a + b < limit:
            not_sum_of_abundant[a+b] = False
        else:
            break

sum( np.where(not_sum_of_abundant)[0] )