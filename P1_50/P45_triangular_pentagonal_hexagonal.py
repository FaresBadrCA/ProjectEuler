"""
Find the smallest number that is triangular, pentagonal and hexagonal

Mathematical facts:
[1] all hexagonal numbers are also triangle numbers, so no need to check the set of triangle numbers

The inverse of the pentagonal number equation is N = (1+ sqrt(1+24*p)) / 6
So if a number 'p' produces an integer 'N' above, then it is a pentagonal number 

Another solution: (props to ke9tv)
pentagonal num = hexagonal num
x(3x-1)/2 == y(2y-1)

3x^2 - 4y^2 - x + 2y = 0

This is a diophantine equation. Runnning a diophantine solver gives:
   m_{i+1} = 97 * m_i + 112 * n_i - 44
   n_{i_1} = 84 * m_i +  97 * n_i - 48


"""


pent_list = [ n*(3*n - 1) // 2 for n in range(500000)  ] 
hex_list = [n*(2*n-1) for n in range(500000)]
result_set = set(hex_list).intersection(set(pent_list))

print ( min( [x for x in result_set if x > 40755] ))

x = 1 # represents the mth pentagonal number
y = 1 # represents the nth hexagonal number
for i in range(10):
   x,y = 97*x + 112*y - 44, 84*x +  97*y - 38
   print( x * (3*x-1) // 2 )

