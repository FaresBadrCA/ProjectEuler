
def chain_length(num, denom ):
    """ return the length of the reciprocal cycle of num/denom """
    dividend_dict = {} # remember previous dividends to identify when we are cycling
    ind = 0
    while True:

        if denom > num: # long division step of moving divisor one decimal spot
            dividend_dict[num] = ind
            num = num * 10
            ind += 1
            continue

        dividend = num % denom
        if dividend == 0: return 0   
        if dividend in dividend_dict: return ind - dividend_dict[dividend]

        dividend_dict[num] = ind
        num = dividend
        continue

L = [0,0] + [ chain_length(1, d) for d in range(2, 1000) ]

import numpy as np
np.argmax(L) # Number with the largest chain
