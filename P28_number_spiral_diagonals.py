"""
Numbers on the top right diagonal are always n^2
The top left diagonal is n^2 - (n-1)
The bottom left diagonal is n^2 - 2*(n-1)
The bottom right diagonal is n^2 - 3*(n-1)

so for any 'n', their sum is 4*n^2 - 6*(n-1)

we want the sum of that for odd n = 1 to 1001
all sums below are for odd values of n only
so sum(4*n^2) - sum(6*(n-1) )
= 4*sum(n^2) - 6 * ( sum(n-1) )

For the square sum, exclude n = 1 from the sum, since the first term does not form a grid, it's just 1
then add 1 to count it back in

for the sum(n-1) we note that this is the sum of even numbers up to n-1
so it's an arithmetic progression that goes 2 + (2+2) + (2+2+2) + ... + (n-1)
"""

def arithmetic_progression(a, d, n):
    """ sum of a + (a+d) + (a+2d) + (a+3d) + ... + I
    with n terms in the series
    """ 
    return ( n * (2*a + (n-1)*d) ) // 2

def sum_sq(n):
    """ 1 + 2^2 + 3^2 + ... + n^2 """
    return n*(n+1)*(2*n+1) // 6

def sum_sq_even(n):
    """ Return the sum of first n even numbers squared. sum( (2k)^2 ) = 4 * sum(k^2) """ 
    return 4 * sum_sq(n)


def sum_sq_odd(n):
    """ Return the sum of first n odd numbers squared. sum( (2n-1)^2 ) = sum of first 2n numbers squared - sum of first n even numbers squared  """
    return sum_sq(2*n) - sum_sq_even(n)


def count_odd(n):
    """ Return count of odd numbers <= n """
    return (n+1) // 2

def count_even(n):
    """ Return count of even numbers <= n """
    return n // 2

n = 1001 # Width of the final grid
k = count_odd(n) # Number of terms we will be adding
ans = 4*(sum_sq_odd(k)-1) + 1 - 6 * arithmetic_progression(2,2, k - 1)
print(ans)

