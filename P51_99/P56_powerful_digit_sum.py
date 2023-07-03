""" find a,b < 100 such that a^b has the maximum digital sum """

def digit_sum(n):
    return sum([int(a) for a in str(n)])


def n_digits(n):
    return len(str(n))

# compute max digit sum
# form an upper limit: 9 * #digits in digit sum 
best_ds = 0
for a in reversed(range(100)):
    n = a ** 99

    if (9*n_digits(n) < best_ds): break

    ds = digit_sum(n)
    best_ds = max(ds, best_ds)


    while 9*n_digits(n) > best_ds: # keep iterating until #digits is too small to possible break our PB 
        n = n // a
        ds = digit_sum(n)
        best_ds = max(ds, best_ds)

