"""
Find the sum of all the multiples of 3 or 5 below 1000.
"""


# bad solution
class MultipleSummer:
    def __init__(self, seed_list, limit = 1000):
        self.result_list = []
        self.seed_list = seed_list
        self.limit = limit
        
    def fill_result_list(self):
        for seed in self.seed_list:
            seed_result = [seed * i for i in range(self.limit) if (seed * i) < self.limit]
            self.result_list.extend(seed_result)
        self.remove_duplicates()
        
    def remove_duplicates(self):
        self.result_list = list(dict.fromkeys(self.result_list))

seed_list = [3,5]
multiple_summer = MultipleSummer(seed_list)
multiple_summer.fill_result_list()

multiple_summer.result_list.sort()
print(multiple_summer.result_list)
print( sum(multiple_summer.result_list) )




#better solution:
sum = 0
for i in range(1,1000):
    if i%3==0 or i%5==0:
        sum += i

print(sum)