"""
let D(a) be the number of digits in 'a'
A requirement is that D(a) + D(b) + D(a*b) = 9

However, D(a*b) is either D(a)+D(b) or D(a)+D(b)-1
if D(a*b) = D(a)+D(b)
then we need 2*D(a) + 2*D(b) = 9
and this cannot be

therefore, D(a*b) must be D(a) + D(b) - 1
therefore, 2*D(a) + 2*D(b) = 10
[1] so D(a) + D(b) = 5

[2] Since D(a*b) = D(a) + D(b) - 1, then the most significant digits of 'a' and 'b' cannot multiply to more than 9
or D(a*b) would have an extra digit. 

That means the most significant digits of a and b must be from this list:
(1,2), (1,3), (1,4), (1,5), (1,6), (1,7), (1,8), (1,9), (2, 3), (2,4)
"""

from itertools import combinations, permutations

def is_pandigital(s:str):
    return len(s) == 9 and set(s) == set('123456789')        

all_digits = set( [1,2,3,4,5,6,7,8,9] )
first_digit_combinations = [ (1,2), (1,3), (1,4), (1,5), (1,6), (1,7), (1,8), (1,9), (2,3), (2,4) ]
result_list = []

for first_digit_comb in first_digit_combinations:
    a_first_digit = str( first_digit_comb[0] )
    b_first_digit = str( first_digit_comb[1] )
    remaining_digits = all_digits - set(first_digit_comb)

    for a_len in range(0, 4): # Append this many digits to the first digit to construct 'a'
        b_len = 5 - a_len - 2 # 5 digits in total, and the first 2 are already acounted for
        for a_digits in combinations(remaining_digits, a_len):
            a_digits = set(a_digits)
            remaining_digits2 = remaining_digits - a_digits 
            for b_digits in combinations(remaining_digits2, b_len):
                for a_p in permutations(a_digits):
                    for b_p in permutations(b_digits):
                        # (a_p) and (b_p) are tuples containing a particular arrangement of digits for 'a' and 'b'
                        a_str = a_first_digit + ''.join(map(str,a_p))
                        b_str = b_first_digit + ''.join(map(str,b_p))
                        a = int(a_str)
                        b = int(b_str)
                        c = a*b
                        if (is_pandigital( a_str + b_str + str(c) )): result_list.append((a,b))



print(sum(set([a*b for a,b in result_list])))


