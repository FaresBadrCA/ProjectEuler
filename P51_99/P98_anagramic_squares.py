""" Find all square anagram word pairs 
Find anagramic square number pairs
and find anagramic english word pairs

For each anagramic pair, produce a 'key' describing the transformation

Iterate through the anagramic square numbers in descending number.
For each number, look up its anagramic key in the set of english words.
Once we find a match, that is our answer
"""

from math import sqrt
from collections import defaultdict
from itertools import combinations 

def get_anagramic_pairs(word_list):
    """ Given a list of strings of identical length, return all pairs of anagrams """
    abc_list = map(lambda word: ''.join(sorted(word)), word_list)
    
    anagram_d = defaultdict(list) # Map an abc sequence to 
    for abc, word in zip(abc_list, word_list):
        anagram_d[abc].append(word)

    pairs = []
    for abc in anagram_d.keys():
        if len(anagram_d[abc]) <= 1: continue
        for c in combinations(anagram_d[abc], 2):
            pairs.append(c)
    return pairs

def get_anagram_key(w1, w2):
    """ Given 2 strings, find a unique key that transforms w1 into w2 """
    result = []
    prev_found_d = {} # Dictionary to remember where characters were found
    for c in w1:
        if c in prev_found_d: new_i = w2.find(c, prev_found_d[c] + 1)
        else: new_i = w2.find(c)
        prev_found_d[c] = new_i
        result.append( str(new_i) )
    return ''.join(result)


words = open("data/0098_words.txt").read().split(sep = "\",\"")
words[0] = words[0][1:]
words[-1] = words[-1][:-1]
eng_anagrams = get_anagramic_pairs(words)

dig_lim = max( map(lambda x: max(len(x[0]), len(x[1]) ), eng_anagrams) )
lim = int(sqrt(10**(dig_lim+1)))
nums = [str(x**2) for x in range(lim, 1, -1)]
num_anagrams = get_anagramic_pairs(nums)
num_anagrams = sorted(num_anagrams, key = lambda x: max( int(x[0]), int(x[1]) ), reverse = True)

eng_keys = defaultdict(list)
for w1,w2 in eng_anagrams:
    eng_keys[ get_anagram_key(w1,w2) ].append((w1,w2))
    eng_keys[ get_anagram_key(w2,w1) ].append((w2,w1))

for n1, n2 in num_anagrams:
    key = get_anagram_key(n1,n2)
    if key in eng_keys:
        for w1,w2 in eng_keys[key]:
            T = str.maketrans(n1,w1)
            if len(T) == len(w1): # No character was reused
                print(n1, n2, w1, w2)

