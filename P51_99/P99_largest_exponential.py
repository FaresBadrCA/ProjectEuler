import math
lines = [ map(int, l.split(',')) for l in open("data/0099_base_exp.txt").read().split('\n')]
n, i = max( [ (e * math.log(b), i) for i,(b,e) in enumerate(lines) ] )
print(i + 1)

