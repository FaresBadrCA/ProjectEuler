# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

def is_palindrome(s:str):
    # return all([s[i] == s[-i-1] for i in range(len(s)//2)])
    return s == s[::-1]

# how do I convert a number to binary?
result_list = []
for i in range(1000000):
    if is_palindrome( str(i) ) and is_palindrome( bin(i)[2:] ): result_list.append(i)


print(sum(result_list))