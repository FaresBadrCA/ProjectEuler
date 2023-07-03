# Find the sum of all numbers which are equal to the sum of the factorial of their digits.

import math

upper_bound = 2540160 # 7 * 9!, so above this number, we are always greater than the digit factorial

factorial_dict = { str(i):math.factorial(i) for i in range(10)}
result_list = [ i for i in range(3,upper_bound) if sum([ factorial_dict[d] for d in str(i)]) == i  ]