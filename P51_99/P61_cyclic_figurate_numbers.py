from collections import defaultdict

f = lambda x : x > 999 and x <= 9999
tria = list(filter(f, [n*(n+1)//2 for n in range(200) ]))
squa = list(filter(f, [n*n for n in range(200) ] ))
pent = list(filter(f, [n*(3*n-1)//2 for n in range(200) ] ))
hexa = list(filter(f, [n*(2*n-1) for n in range(200) ] ))
hept = list(filter(f, [n*(5*n-3)//2 for n in range(200) ] ))
octa = list(filter(f, [n*(3*n-2) for n in range(200) ] ))
figs = [tria, squa, pent, hexa, hept, octa]

first_2digits = lambda n: n // 100
last_2digits = lambda n: n % 100

d = defaultdict(list) # dictionary mapping two-digit numbers to list of figurate numbers starting with those digits
for i, L in enumerate(figs):
    for n in L:
        d[ first_2digits(n) ].append((i,n))

# a chain is a tuple: (set of remaining figurate indeces, list of numbers in chain)
# Chain is cyclic so we can choose any figurate number to start from. We choose triangular numbers.
chains = [ (set(range(1,6)), [n])  for n in tria]
next_chains = []
for _ in range(5):
    for allowed_i, n_list in chains:
        last_digits = last_2digits(n_list[-1])
        for fig_i, n in d[last_digits]:
            if fig_i in allowed_i:
                next_allowed_i = allowed_i.copy()
                next_allowed_i.remove(fig_i)
                next_n_list = n_list.copy()
                next_n_list.append(n)
                next_chains.append( (next_allowed_i, next_n_list) )
    chains, next_chains = next_chains, []

result = [c for c in chains if last_2digits(c[1][-1]) == first_2digits(c[1][0])]
print(sum(result[0][1]))
