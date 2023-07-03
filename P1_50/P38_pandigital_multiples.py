"""
Idea: For each value of 'k', find all numbers N such that [N*1][N*2][N*3]...[N*k] are 1-9 pandigital

for k = 2: N cannot be 5 digits because the concatenation of the results will have 10 or 11 digits
N cannot be 3 digits because the concatenation of the results will be 6-7 digits
therefore, N has 4 digits. Additionally, the first digit must be >= 5, so that 2*N produces the 9th digit

for k = 3, N must be 3 digits and the first digit cannot be greater than 3, or we would produce a tenth digit in the answer
for k = 4, N cannot be 3 digits
"""

def is_pandigital(s:str):
    return len(s) == 9 and set(s) == set('123456789')


result_list = []
k = 2
for n in range(5000, 10000):
    concatenated_product = ''.join([str( (m+1)*n) for m in range(k)])
    if is_pandigital(concatenated_product): result_list.append( [n,k, int(concatenated_product)] )

k = 3
for n in range(100, 400):
    concatenated_product = ''.join([str((m+1)*n) for m in range(k)])
    if is_pandigital(concatenated_product): result_list.append( [n,k, int(concatenated_product)] )

for k in range(4,7):
    for n in range(100):
        concatenated_product = ''.join([str((m+1)*n) for m in range(k)])
        if is_pandigital( concatenated_product ): result_list.append( [n,k, int(concatenated_product)] )


print( sorted(result_list, key = lambda x: x[2], reverse = True)[0][2] )





