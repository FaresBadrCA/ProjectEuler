"""
What is the maximum 16-digit string for a "magic" 5-gon ring?

We concatenate 15 numbers. '10' has to be in the outer ring to get a 16-digit number, otherwise we get 17-digits.
To get the maximum string, the other outer numbers should be 10,9,8,7,6.

lower bound: 10+1+2 = 13
upper bound: 6+5+4 = 15

other observation: 10+9+8+7+6+(2*(1+2+3+4+5)) = 70 -> dividing by 5 -> means each side should sum to 14

"""

from itertools import permutations

def check_magic(outer_ring, inner_ring, s):
    return all( outer_ring[i] + inner_ring[i] + inner_ring[i+1] == s for i in range(4) )

def get_string(outer_ring, inner_ring):
    s = []
    # get index of smallest value in outer ring
    i = outer_ring.index(min(outer_ring))
    for _ in range(5):
        s.append( str(outer_ring[i]) )
        s.append( str(inner_ring[i]) )
        i = (i+1)%5
        s.append( str(inner_ring[i]) )
    return ''.join(s)


digits = list(range(10,0,-1))
inner_d = set([1,2,3,4,5])
outer_d = set([10,9,8,7,6])

lbound = 10+1+2 # 13
ubound = 6+5+4 # 15

inner_permutations = list(permutations(inner_d))
outer_permutations = list(permutations(outer_d))

max_str = ''
for outer_ring in outer_permutations:
    for inner_ring in inner_permutations:    
        s = outer_ring[-1] + inner_ring[-1] + inner_ring[0]
        if s < lbound or s > ubound: continue

        if check_magic(outer_ring, inner_ring, s):
            cur_str = get_string(outer_ring, inner_ring)
            if cur_str > max_str: max_str = cur_str

print(max_str)