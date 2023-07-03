import numpy as np

N = int(1e7) # number of rounds of the game
dice_rolls = list( zip( np.random.randint(low = 1, high = 4, size = N), np.random.randint(low = 1, high = 4, size = N) ) )
RNG = np.random.randint(low = 1, high = 16, size = N)

board_sz = 40
CC = set((2,17,33))
CH = set((7,22,36))
R = [5, 15, 25, 35]
U = [12, 28]
d = [0]*board_sz # number of times each square was visited

def goto_first(pos, L):
    """ Given a position, pos, and a sorted list of positions, L,
    return the first value in L greater than pos. Otherwise, returns the first value in L
    """
    for val in L:
        if val > pos: return val
    return L[0]

pos = 0
double_count = 0
for i in range(N):
    d1, d2 = dice_rolls[i][0], dice_rolls[i][1]
    if d1 == d2: double_count += 1
    else: double_count = 0

    pos = (pos + d1 + d2) % board_sz
    rand = RNG[i]

    if pos in CC:
        if rand == 1: pos = 0
        elif rand == 2: pos = 10

    elif pos in CH:
        if rand == 1: pos = 0
        elif rand == 2: pos = 10
        elif rand == 3: pos = 11 # C1
        elif rand == 4: pos = 24 # E3
        elif rand == 5: pos = 39 # H2
        elif rand == 6: pos = 5 # R1
        elif rand == 7 or rand == 8: pos = goto_first(pos, R)
        elif rand == 9: pos = goto_first(pos, U)
        elif rand == 10: 
            pos = (pos - 3) % board_sz
    
        if pos == 30 or double_count == 3: pos = 10

    d[pos] += 1


a,b,c = sorted(d, reverse = True)[:3]
''.join( [ str(d.index(x)).zfill(2) for x in [a,b,c]] )

print([d.index(x) for x in sorted(d, reverse = True)])


