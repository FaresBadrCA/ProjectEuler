
# If we can write a test function, then we're only testing about 10,000 numbers which is fairly easy
import math
import numpy as np

def is_cancelling(num, denom):
    """ Return true if cancelling the same digit from num and denom keeps num/denom the same """
    
    shared_digits = list( set(str(num)).intersection(set(str(denom))) )
    if not shared_digits:
        return False

    shared_digit = shared_digits[0] # a string
    q1 = num / denom

    # remove the shared digit from both numbers
    num = int( str(num).replace(shared_digit, '', 1) )
    denom = int( str(denom).replace(shared_digit, '', 1) )

    if (denom == 0): return False
    q2 = num / denom

    if math.isclose(q1, q2): return True
    return False


result_list = []
for i in range(10,100):
    for j in range(i+1,100):
        if i%10 == 0 and j%10 == 0: continue
        if is_cancelling(i, j): result_list.append( [i,j] )


num = math.prod( [a for a,b in result_list] )
denom = math.prod( [b for a,b in result_list] )

gcd = math.gcd(num, denom)

print(denom / gcd)

