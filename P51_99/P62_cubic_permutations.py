i = 1
d = {}
while True:
    n_str = ''.join(sorted(str(i**3)))
    d.setdefault(n_str, []).append(i)
    i += 1
    if len(d[n_str]) == 5: break

print(min(d[n_str]) ** 3)
