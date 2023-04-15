"""
we want to find all 0-9 pandigital numbers with some given properties

general idea: go through the properties one at a time
produce a set of numbers satisfying the first property

then produce a set of numbers satisfying the seconds property

find pairs of numbers satisfying properties 1 and 2 at the same time without repeating digits

continue with third property, etc.
"""

from itertools import product

def is_nonrepeating(L:list):
    """ given a list of numbers, check that none of them repeat """
    return len(set(L)) == len(L)

def n_to_3_digit_list(n):
    return [(n//100)%10, (n//10)%10, n%10]

divisor_list = [2, 3, 5, 7, 11, 13, 17]
p_list = [] # List of lists, where the inner list has candidate set of digits with desired properties
for k in divisor_list:
    p_list.append(
        [ n_to_3_digit_list(i) for i in range(k, 1000, k) if is_nonrepeating(n_to_3_digit_list(i)) ] # multiples of k without repeating digits
    )

p = p_list.pop() # p will be the final list with the pandigital numbers. we start with digits 10,9,8. Then we add 1 digit per iteration
for prev_p in reversed(p_list):
    p = [ a[0:1] + b for a,b in product(prev_p,p) if a[1] == b[0] and a[2] == b[1] and is_nonrepeating(a[0:1] + b)]

digits_set = set(range(10))
first_digits = [ list(digits_set - set(L)) for L in p ] # list of lists of size 1 containing first digit of each pandigital number
pandigital_list = [ int( ''.join(map(str,a+b))) for a,b in zip(first_digits, p)]

print(sum(pandigital_list))

