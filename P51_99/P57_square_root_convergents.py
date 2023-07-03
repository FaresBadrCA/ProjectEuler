""" let x_i be the ith fractional expansion for sqrt(2)
    Let y_i be x_i - 1
    Let y_i = n_i / d_i

    We notice that d{i+1} = 2*d_i + n_i, and n{i+1} = d{i} 
"""

i = 1 
n = 1
d = 2

def n_digits(n):
    return len(str(n))

count = 0
while i <= 1000:
    i += 1
    d, n = 2*d + n, d
    if len(str(d + n)) > len(str(d)):
        count += 1
    
print(count)
        