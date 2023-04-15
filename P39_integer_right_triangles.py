"""
p is the perimeter of a right-triangle of sides {a,b,c}

p = a+b+c 
a^2 + b^2 = c^2
"""

import numpy as np
p_lim = 1000
p_count_dict = {} # count the number of times 
for a in range(1, p_lim):
    for b in range(a, p_lim - a):
        c = np.sqrt(a**2 + b**2)
        p = a+b+c
        if (p > p_lim): break # Stop looping through 'b', as perimeter is too big
        
        if c.is_integer():
            if p in p_count_dict:
                p_count_dict[p] += 1
            else:
                p_count_dict[p] = 1

# Find key in p_count_dict with the highest value. That is perimeter with the highest number of occurrences
print ( max(p_count_dict, key = p_count_dict.get) )
