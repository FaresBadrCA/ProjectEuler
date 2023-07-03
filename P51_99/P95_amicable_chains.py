from math_utils import sum_of_divisors_array
import networkx as nx

lim = int(1e6)
dsum = sum_of_divisors_array(lim)

G = nx.DiGraph()
G.add_edges_from( zip(range(lim+1), dsum) )
longest_cycle = sorted(nx.simple_cycles(G), key = lambda x : len(x), reverse = True )[0]
print(min(longest_cycle))
