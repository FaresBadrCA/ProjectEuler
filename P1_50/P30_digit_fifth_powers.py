# Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

# that is, x = digit1^5 + digit2^5 + digit3^5 + ... for all its digits

def sum_digit_powers(n, k):
    """ 123 -> 1^k + 2^k + 3^k """
    ans = 0
    while n > 0:
        n, q = divmod(n, 10) # divide by 10. The remainder is the rightmost digit
        ans += q**k
    return ans


k = 5
# First, we discover an upper limit  for the search
# That is a number N such that for all numbers n > N, n > sum_digit_powers(n, k)
limit = 999
while sum_digit_powers(limit, k) > limit:
    limit = limit * 10 + 9


numlist = [x for i, x in enumerate( [sum_digit_powers(n,k) for n in range(limit)  ] ) if x == i ]
numlist = [x for x in numlist if x > 1]

print(sum(numlist))
