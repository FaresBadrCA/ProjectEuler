from math import factorial

digfact_d = { i : factorial(i) for i in range(0,10) }
len_d = {} # dictionary mapping numbers to their chain length
for i in range(1000000):
    chain = []
    n = i
    while n not in len_d:
        chain.append(n)
        len_d[n] = 0
        n = sum( digfact_d[int(c)] for c in str(n) )
    
    L = len(chain) + len_d[n] # chain length of 'i', which is chain[0] if it's in the chain
    i = 0
    while i < len(chain):
        k = chain[i]
        if k == n:
            L = L - i # all remaining terms in the chain will have this cycle length
            break
        len_d[k] = L - i
        i += 1

    while i < len(chain): # rest of the chain is part of the same cycle, they have the same cycle length
        k = chain[i]
        len_d[k] = L
        i += 1


result_list = [x for x, L in len_d.items() if L == 60]
print(len(result_list))