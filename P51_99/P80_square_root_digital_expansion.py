from math import isqrt
import mpmath
mpmath.mp.dps = 105

result = 0
lim = 100
for i in range(2, lim):
    if isqrt(i) * isqrt(i) == i: continue
    s = str(mpmath.sqrt(i))
    result += sum( int(x) for x in s[:101] if x !='.' )

print(result)
