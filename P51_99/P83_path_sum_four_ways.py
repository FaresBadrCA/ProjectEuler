# See "Daijkstra'a algorithm"
import heapq

lines = open(r'data\p083_matrix.txt').readlines()
lines = [ list(map(int, line[:-1].split(','))) for line in lines] # list of lists of strings

d = {} # maps coordinates (row, col) to minimal path sum found so far
max_r = len(lines) - 1
max_c = len(lines[0]) - 1

PL = [(0,0,0)] # A queue of positions left to search and the value we have when searching them (v,r,c)
while PL:
    v,r,c = heapq.heappop(PL) # explore the current position
    v += lines[r][c]

    if (r,c) in d and d[(r,c)] <= v: continue # better path through this node was already explored
    else: d[(r,c)] = v

    if r < max_r: heapq.heappush(PL, (v,r+1,c)) # heap structure explores the lowest cost nodes first
    if c < max_c: heapq.heappush(PL, (v,r,c+1))
    if r > 0: heapq.heappush(PL, (v,r-1,c))
    if c > 0: heapq.heappush(PL, (v,r,c-1))

print( min( [x for (r,c), x in d.items() if c == max_c and r == max_r] ) )