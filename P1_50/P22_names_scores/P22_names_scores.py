import os
from sys import path

f = open( os.path.join(os.getcwd(), "P22_names_scores" ,"names.txt"), "r")
s = f.read()
s = s.replace('"' , '' ) # delete quotes
name_list = s.split(",")

name_list = sorted(name_list)

# assume all letters are capital
letter_score = lambda char: ord(char) - ord('A') + 1
name_scores = [ (i+1) * sum([letter_score(char) for char in name]) for i, name in enumerate(name_list) ]
print(sum(name_scores))
