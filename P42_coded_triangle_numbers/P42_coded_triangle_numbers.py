# How many words in the file are triangle words
# 
import os
from sys import path

f = open( os.path.join(os.getcwd(), "P42_coded_triangle_numbers" ,"P42_words.txt"), "r")
s = f.read()
s = s.replace('"' , '' ) # delete quotes
word_list = s.split(",")

letter_score = lambda char: ord(char) - ord('A') + 1
word_score = lambda word: sum( [letter_score(letter) for letter in word] )

word_score_list = [word_score(word) for word in word_list]

upper_bound = max(word_score_list) # highest word score

triangle_nums = set()
t = 0
n = 1
while t <= upper_bound:
    t = t + n
    triangle_nums.add(t)
    n += 1

len ( [n for n in word_score_list if n in triangle_nums] )
