class PathCounter:
    def __init__(self):
        self.cache = {} # Memoization

    def num_paths(self, x, y):
        """ Given number of steps left in x and y directions, return # possible routes """
        
        # Make sure x >= y, to not have to repeat the same calculation twice
        if y > x:
            x , y = y, x

        if (x,y) in self.cache:
            return self.cache[ (x,y) ]
        
        if x == 1:
            return y + 1

        if y == 1:
            return x + 1

        right_paths= self.num_paths(x - 1, y)
        down_paths  = self.num_paths(x, y - 1)

        self.cache[ (x,y) ] = right_paths + down_paths
        return right_paths + down_paths 



path_counter = PathCounter()
print ( path_counter.num_paths(20,20) )

# COMBINATORIAL SOLUTION: for an mxn grid, we make 'm + n' moves, of which 'm' of them are down. 
# From 'm+n' slots, how many ways can we choose 'm' of them? It's (m+n Choose m)
# for nxn grid: (2n choose n) = (2n)! / (n! * n!) 

from math import comb
print( comb(40, 20) )