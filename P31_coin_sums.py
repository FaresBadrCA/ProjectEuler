class CoinCounter:
    def __init__(self, denominations:list):
        self.coins = denominations
        self.result_cache = {}

    def count_combinations(self, n, ind):
        """ Return the number of combinations of coins from coin_list that add up to n exactly 
        To not count different orderings of the same combination of coins, we restrict the order in which we pull coins
        so that we never pick a coin smaller than one we previously picked.

        Thus, we only pick coins after ind
        Recursive solution works, but is limited by recursion depth
        """

        if (n, ind) in self.result_cache: return self.result_cache[ (n,ind) ]

        n_combinations = 0
        for i in range(ind, len(self.coins) ):
            coin = self.coins[i]
            remaining_n = n - coin

            if remaining_n < 0: continue

            if remaining_n == 0: 
                n_combinations += 1
                continue

            n_combinations += self.count_combinations(remaining_n, i)

        self.result_cache[ (n,ind) ] = n_combinations
        return n_combinations


denominations = [1, 2, 5, 10, 20, 50, 100, 200]
#N = 200 
#counter = CoinCounter(denominations)
#counter.count_combinations(N, 0)

### Alternative solution
N = 200
ways = [0] * (N+1)
ways[0] = 1;
for coin in denominations:
    for j in range(coin, N+1, 1):
        ways[j] += ways[j - coin];

print(ways[-1])