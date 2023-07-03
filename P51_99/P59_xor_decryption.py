from itertools import groupby

f = open('data/p059_cipher.txt')
s = f.readline().split(sep = ',')

# Sorted list of characters that appear in the cipher, in descending order of their frequency
enc_sorted = sorted( [(len(list(lst)),v) for v,lst in groupby(sorted(s))], reverse = True )
enc_sorted = [c[1] for c in enc_sorted]

# The most common character will be an encrypted space. It will be the most common three times, once for each letter in the password
c0 = int(enc_sorted[0]) ^ ord(' ')
c1 = int(enc_sorted[1]) ^ ord(' ')
c2 = int(enc_sorted[2]) ^ ord(' ')
pwd = [c0,c1,c2] # The order might be incorrect

unenc = [ chr( int(c) ^ pwd[(i+1)%3]) for i,c in enumerate(s) ]
print(sum( [ord(c) for c in unenc] ))
