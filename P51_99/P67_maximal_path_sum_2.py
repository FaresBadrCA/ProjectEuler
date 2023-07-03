"""
See Dijkstra's algorithm and Bellman-ford
"""
class Tree:
    def __init__(self, lines):
        """ Initialize from list of strings, where each string is a line of the triangle """
        # Hash table with the optimal path. It maps (DEPTH, INDEX) tuples to their optimal score
        self.optimal_paths = {}
        self.numlist = [ list(map(int, line[:-1].split())) for line in lines ] # List of lists, where each inner list represents a line. Usage: numlists[DEPTH][INDEX]
        self.MAX_DEPTH = len(self.numlist)


    def explore(self, depth, ind, score):
        """
       Enter a position (specified by depth,ind) with a given score, then increase the score
       and check if we need to keep exploring this route based on previous search results
       """
        if depth >= self.MAX_DEPTH:
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


f = open(r'data/p067_triangle.txt')
lines = f.readlines()
tree = Tree(lines)
tree.explore(0,0,0)
print(max(tree.optimal_paths.values()))