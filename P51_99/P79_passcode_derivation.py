"""
I mis-interpreted the problem! I thought the entered numbers are the consecutive characters in the password and characters can be repeated.
it turns out the entered numbers are not necessarily consecutive, just that the later numbers occur later in the actual password.
Another very important piece of information not mentioned is that the 
"""

f = open(r'data/p079_keylog.txt')
s = f.read().split('\n')[:50]
s = list(set(s)) # remove duplicates

d = {} # map characters to ones that precede them

for n in s:
    if n[0] not in d: d[n[0]] = set()
    for i in range(1,3):
        if n[i] not in d: d[n[i]] = set()
        d[n[i]].add(n[i-1])

pwd = ''
while d:
    digit = min(d, key = lambda x: len(d.get(x)) )
    del(d[digit])
    for set_ in d.values():
        if digit in set_: set_.remove(digit)
    pwd = pwd + digit

