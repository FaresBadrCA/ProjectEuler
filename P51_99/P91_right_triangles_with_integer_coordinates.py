""" How many right triangles can be formed  
Try all possible triangles: For each one, test the dot product of the vectors representing their sides.
If the dot product is zero, we have two perpendicular sides, so it's a right triangle

In the forums, JosefFruhauf has an interesting way of calculating it:
First, there is the set of triangles where the two points are on the x and y axis
those are of the form (x,0)(x,y), or  (0,y)(x,y), or (x,0)(0,y) , and each group has n^2 possible values, so there are 3n^2 such triangles

The next type of triangle has its right-angle vertex Q = (a,b) where a,b > 0.
The other point, P = (x,y) must be such that it lies on the line perpendicular to OQ.

OQ's equation is y = (a/b)x + b
so P lies on the line: y = -(a/b)x + b
Moving some terms around: ax + by = a^2 + b^2
Which is a diophantine equation where one solution is (a,b).

vid on solving diophantine equations: https://www.youtube.com/watch?v=JBnKs15Vvg8

Letting d = gcd(a,b), solutions to this are diophantine equation are:
x = a - (b/d)*k
y = b + (a/d)*k

By considering only points to the left side of OQ, we restrict x and y, and the result can be multiplied by 2 for points to the right of OQ by symmetry:
0 <= x < a,    b < y <= n


plugging in the solutoins to the restrictions above: k > 0      and     a(d/b) >= k     and  k <= (n-b)*(d/a)
so 1 <= k <= min( a(d/b),  (n-b)*(d/a) )
The restriction above gives the count of possible values of k for a given (a,b). We sum over all possible combinations of (a,b) and we're done.

TOTAL = 3n^2 + 2* sum{1 <= a,b <=n} ( min( ad/b, (n-b)(d/a) )  )

"""

from itertools import product

c = 0
lim = 50

for x1, y1 in product( range(lim+1), range(lim+1) ):
    if x1 == 0 and y1 == 0: continue
    for x2, y2 in product( range(lim+1), range(lim+1) ):
        if x1 == x2 and y1==y2: continue
        if x2 == 0 and y2 == 0: continue
        if ( x1*x2 + y1*y2 == 0) or ( x1*(x2-x1) + y1*(y2-y1) == 0 ) or ( x2*(x2-x1) + y2*(y2-y1) == 0 ):
            c += 1

print(c//2) # Each triangle gets counted twice