triangle = \
r"""75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
"""


# Make a tree object that takes in a string 
class Tree:
    def __init__(self, triangle):
        """ Initialize from string representing the triangle of numbers """
        # Hash table with the optimal path. It maps (DEPTH, INDEX) tuples to their optimal score
        self.optimal_paths = {}
        
        self.numlist = [] # List of lists, where each inner list represents a line. Usage: numlists[DEPTH][INDEX]
        for depth, line in enumerate( triangle.splitlines() ):
            s = [ int(line[3*i:3*i+2]) for i in range(depth + 1) ] # Assumes all numbers are 2-digit
            self.numlist.append(s)

        self.MAX_DEPTH = depth

    def explore(self, depth, ind, score):
        """
       Enter a position (specified by depth,ind) with a given score, then increase the score
       and check if we need to keep exploring this route based on previous search results
       """
        if depth > self.MAX_DEPTH:
            return

        score += self.numlist[depth][ind]

        if (depth, ind) in self.optimal_paths:
            old_score =  self.optimal_paths[(depth, ind)]
            if score > old_score:
                self.optimal_paths[(depth, ind)] = score
            else:
                return # We've already reached this node before with an equal/better score, no need to keep exploring
        else:
            self.optimal_paths[(depth, ind)] = score

        self.explore(depth + 1, ind, score)
        self.explore(depth + 1, ind + 1, score)

tree = Tree(triangle)
tree.explore(0,0,0)
max(tree.optimal_paths.values())