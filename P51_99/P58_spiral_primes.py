""" 
Expand a spiral until less than 10% of its diagonals have prime numbers.

Properties: 
- Spiral length will be odd numbers. 1->3->5->7->9 ...
- For a spiral of length (2n+1), there will be n numbers in each diagonal, for a total of 4*n + 1 numbers (the +1 is because of the '1' in the center)
- numbers in the bottom right diagonal are (2n+1)^2
- numbers in the bottom left diagonal are (2n+1)^2 - 2n, and top left is (2n+1)^2 - 4n, and top right is (2n+1)^2 - 6n

idea: iterate through 'n' and generate diagonal numbers and keep count of how many are prime.
"""

from math_utils import simple_sieve

n_lim = int(1e9) # assume we won't need primes above this limit
is_prime_arr = simple_sieve(n_lim)

prime_count = 0
n = 0
while True:
    n += 1
    temp = (2*n+1)**2
    bot_left, top_left, top_right = temp - 2*n, temp - 4*n, temp - 6*n
    if (is_prime_arr[bot_left]): prime_count += 1
    if (is_prime_arr[top_left]): prime_count += 1
    if (is_prime_arr[top_right]): prime_count += 1

    if prime_count / (4*n+1) < 0.1:
        break

print(2*n + 1)