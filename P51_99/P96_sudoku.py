""" Solve sudoku with a tree search that explores empty spots with the smallest number of possible values first """

class Sudoku():
    def __init__(self, grid):
        """ Grid: list of strings, such that grid[row][col] is the value at that position """
        self.g = grid
        self.all_possible = set(map(str,range(1,10)))
        self.v_sets = [] # v_sets[i] is the set of possible values in column i
        self.h_sets = [] # h_sets[i] is the set of possible values in row i

        for c in range(9):
            s = set()
            for r in range(9):
                s.add(self.g[r][c])
            self.v_sets.append(self.all_possible.difference(s))

        for r in range(9):
            s = set()
            for c in range(9):
                s.add(self.g[r][c])
            self.h_sets.append(self.all_possible.difference(s))

        # sq_sets[R][C] is the set of possible values for a spot with position (r,c), such that r//3 = R and c//3 = C 
        self.sq_sets = [ [ [],[],[] ] for _ in range(3) ] # 3x3 matrix
        for R in range(3):
            for C in range(3):
                s = set()
                for r in range(3):
                    for c in range(3):
                        s.add(self.g[3*R + r][3*C + c])
                self.sq_sets[R][C] = self.all_possible.difference(s)

        self.z = self.get_empty_spots() # list of tuples each representing a zero in the grid: (row, col, possible values)

    def get_empty_spots(self):
        """ Return list of empty spots sorted (descending) by #Possible values: (row, col, Set of possible values) """ 
        z_list = []
        for r in range(9):
            for c in range(9):
                if self.g[r][c] == '0':
                    z_list.append( (r,c, self.v_sets[c].intersection(self.h_sets[r]).intersection(self.sq_sets[r//3][c//3]) ) )
        return sorted(z_list, key = lambda x: len(x[-1]), reverse = True)

    def place_number(self, n: str, r: int, c: int):
        self.g[r] = self.g[r][:c] + n + self.g[r][c+1:]
        self.v_sets[c].remove(n)
        self.h_sets[r].remove(n)
        self.sq_sets[r//3][c//3].remove(n)

    def unplace_number(self, r, c):
        n = self.g[r][c]
        self.g[r] = self.g[r][:c] + '0' + self.g[r][c+1:]
        self.v_sets[c].add(n)
        self.h_sets[r].add(n)
        self.sq_sets[r//3][c//3].add(n)

    def is_possible(self, n, r, c):
        """ Return True if we can place the number n in spot (r,c) """
        return (n in self.v_sets[c]) and (n in self.h_sets[r]) and (n in self.sq_sets[r//3][c//3])

    def solve(self):
        """ Return True if the grid is solved, False if it cannot be solved  """     
        played = [] # List of played moves in this branch of the tree
        while self.z:
            r,c, n_set = self.z.pop()

            if len(n_set) == 1:
                n = n_set.pop()
                if self.is_possible(n,r,c):
                    self.place_number(n,r,c)
                    played.append((r,c))
                    self.z = self.get_empty_spots()
                    continue
                else:
                    for r,c in played:
                        self.unplace_number(r,c)
                    return False

            for n in n_set:
                if self.is_possible(n,r,c):
                    self.place_number(n, r, c)
                    self.z = self.get_empty_spots()
                else:
                    continue

                if self.solve(): 
                    return True
                else:
                    self.unplace_number(r,c)
                    self.z = self.get_empty_spots()
            else: # Tried all possible values and non lead to a solution
                for r,c in played: 
                    self.unplace_number(r,c)
                return False
        else:
            return True # No more zeroes, so solution is found

import re
fn = "data/p096_sudoku.txt"
lines = open(fn).read()
lines = re.split("Grid \d*\n", lines)[1:]
results = []
for line in lines:
    g = line.replace('\n', '')
    g = [ g[i:i+9] for i in range(0, 9*9, 9) ] # game grid: list of strings, g[row][col]
    S = Sudoku(g)
    _ = S.solve()
    results.append(int( S.g[0][:3] ))

print(sum(results))