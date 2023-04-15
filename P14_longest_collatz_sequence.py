class CollatzChainer:
    def __init__(self):
        self.cache = {1:1} # Memoization

    def chain_length(self, n: int) -> int:
        """ Return length of a collatz chain for a number n """
        if n in self.cache:
            return self.cache[n]

        if (n % 2 == 0):
            L = self.chain_length(n / 2) + 1
            self.cache[n] = L
            return L
        else:
            L = self.chain_length( (3*n + 1) / 2) + 2 # Optimization of doing two collatz steps in one
            self.cache[n] = L
            return L

    def max_chain(self) -> tuple:
        """ Return tuple (Number with Largest Chain, Chain Length) """
        n = max(self.cache, key = self.cache.get)
        return (n, self.cache[n])


chainer = CollatzChainer()
limit = 1000000
# Longest chain always in latter half
for i in range(int(limit / 2), limit, 1):
    L = chainer.chain_length(i)

print (chainer.max_chain())