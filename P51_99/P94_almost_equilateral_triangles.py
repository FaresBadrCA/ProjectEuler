# A = (a+1)/4 * sqrt((3a+1)(a-1))
# 'a' has to be odd for (a+1)/4 to be an integer. let a = 2b - 1
# A = 2b/4 * sqrt((6b-2)(2b-2)) = b/2 * sqrt( 2*2*(3b-1)(b-1) ) = b*sqrt((3b-1)(b-1))
# Need (3b-1)(3b-1) to be a square number: (3b-1)(b-1) = t^2
# => 3b^2 - 4b + 1 = t^2 
# => 3b^2 - 4b + 1 - t^2 = 0

# b = ( 4 +- sqrt( 16 - 12*(1-t^2) ) )/ 6
# b = 4 +- sqrt( 4(1 - 3t^2) ) / 6
# b = 2/3* (1 + sqrt ( 1-3t^2 ) )

# want 1-3t^2 to be a square
# r^2 = 1-3t^2
# r^2 + 3t^2 = 1
# solve pell's equation for (r,t), and plug in 't' above to get 'b', which gives us 'a'

from math import isqrt

lim = int(1e9)
a = 3 # side length. (1,1,2) triangle does not exist, so we start with a = 2
result = 0
while a < lim // 3: # Iterate through possible side lengths
    t = (a-1) * (3*a + 1)
    sqrt_t = isqrt(t)
    if sqrt_t**2 == t and (a+1)*sqrt_t % 4 == 0:
        result += 3*a + 1
        print(a, a+1)

    t = (a+1) * (3*a - 1)
    sqrt_t = isqrt(t)
    if sqrt_t**2 == t and (a-1)*sqrt_t % 4 == 0:
        result += 3*a - 1
        print(a, a-1)

    a += 2