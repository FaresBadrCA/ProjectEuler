lines = open(r'data\p081_matrix.txt').readlines()
lines = [ list(map(int, line[:-1].split(','))) for line in lines] # list of lists of strings

d = {} # maps coordinates (col, row) to minimal path sum found so far
max_c = len(lines[0])
max_r = len(lines)


def search(val, col, row):
    v = val + lines[col][row]
    if (col,row) in d and d[(col,row)] <= v: return # better path through this node was already explored
    else: d[(col,row)] = v
    
    if col < max_c - 1:
        search(v, col + 1, row)

    if row < max_r - 1:
        search(v, col, row + 1)
   
    return 


search(0, 0, 0)
print(d[(79,79)])
