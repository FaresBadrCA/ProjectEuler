fib = [1,1]
d = fib[-2]
n_digits = 1000
limit = 10 **(n_digits - 1)
while d < limit:
    d = d + fib[-2]
    fib.append( d )

print( len(fib) )
