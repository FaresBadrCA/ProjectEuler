# -*- coding: utf-8 -*-
"""
What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

idea: we check if the last 'i' elements are in descending order
if not, we call permute(arr, i-1), and its job is to make them in descending order

once permute(arr, i-1) returns True, we have an array in descending order
then we 
1) reverse it so it's in ascending order again
2) find the smallest element larger than k and swap it with k
and call permute again on the result

eventually, there is no elemnet larger than k, then we just return true.

012345
012354
012435
012453
012534
012543
013245 *
013254
013425
013452
013524
013542
014235*
"""

def is_descending(arr):
    return all( [ arr[i] > arr[i+1] for i in range(len(arr) - 1)] )

# given an ascending-order sorted list, return the index of first element greater than k 
# return null if no value is greater than k in L
def ind_greater_than_k(L, k):
    for ind, val in enumerate(L):
        if val > k:
            return ind
    return None


global COUNTER
COUNTER = 1

# returns True when last i elements of the array are in descending order
def permute(arr, i):
    global COUNTER
    if (is_descending(arr[-i:])):
        return True
    
    if (i == 2):
        arr[-1], arr[-2] = arr[-2], arr[-1] # swap the 2 elements
        COUNTER = COUNTER + 1
        if (COUNTER == 1000000):
            print(arr)
        return True # done permuting

    while True:    
        while (not permute(arr, i-1)):
            pass # Keep permuting until last i-1 elements are in descending order

        k = arr[-i]
        greatest_element = arr[-(i- 1)]
        
        if (k > greatest_element):
            return True # last i elements are in descending order
        
        arr[-(i-1):] = reversed(arr[-(i-1):]) # reverse last (i-1) elements
        
        # swap first element greater than k with k
        j = i - ind_greater_than_k(arr[-i:], k)
        arr[-j], arr[-i] = arr[-i], arr[-j]
        COUNTER = COUNTER + 1
        if (COUNTER == 1000000):
            print(arr)


arr = [0,1,2,3,4,5,6,7,8,9]
permute(arr, len(arr))