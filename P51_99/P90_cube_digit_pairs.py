""" Generate all possible combinations of dice faces, and test each one if it is able to represent  """

from itertools import combinations

digits = tuple(str(x) for x in range(10))
comb = sorted(list(combinations(digits,6))) 
sq_arr = [ str(i**2).zfill(2) for i in range(1,10) ]

count = 0
for i in range(len(comb)):
	if '6' in comb[i]: comb[i] = comb[i] + ('9',)
	if '9' in comb[i]: comb[i] = comb[i] + ('6',)
	d1 = comb[i]
	for j in range(i+1): # d1 > d2 to avoid double counting
		d2 = comb[j]
		for sq1, sq2 in sq_arr:
			if not ( (sq1 in d1 and sq2 in d2) or (sq1 in d2 and sq2 in d1) ):
				break
		else: # all square numbers were represented by the die
			count += 1

print(count)