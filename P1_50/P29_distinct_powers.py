numlist = []
for a in range(2, 100 + 1, 1):
    for b in range(2, 100 + 1, 1):
        numlist.append( a**b )

numset = set(numlist)