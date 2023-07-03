""" How many lychrel numbers are there below 10,000 """

def is_palindrome(n):
    return str(n) == (str(n))[::-1]


def rev_add(n):
    return n + int( (str(n))[::-1] )

count = 0
for i in range(10000):
    n = i
    is_lychrel = True
    for j in range(50):
        n = rev_add(n)
        if is_palindrome(n): 
            is_lychrel = False
            break

    if is_lychrel: count += 1
