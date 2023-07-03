lines = open(r'data\p082_matrix.txt').readlines()
lines = [ list(map(int, line[:-1].split(','))) for line in lines] # list of lists of strings

d = {} # maps coordinates (col, row) to minimal path sum found so far
max_c = len(lines) - 1
max_r = len(lines[0]) - 1


def search(val, row, col):
    v = val + lines[row][col]
    if (row,col) in d and d[(row,col)] <= v: return # better path through this node was already explored
    else: d[(row,col)] = v
    
    if col < max_c:
        search(v, row, col + 1)

    if row < max_r:
        search(v, row + 1, col)
    
    if row > 0:
        search(v, row - 1, col)
        
    return 


for i in range(max_r + 1):
    search(0, i, 0)

min( [x for (r,c), x in d.items() if c == max_c] )


