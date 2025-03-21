'''
Write a Python function findCommonElements(L1, L2) that accepts two integer lists L1 and L2 of same length n and return a list that contains elements that are common to both lists. Write a efficient solution that runs in O(nlogn) or better time.

L1 contains all distinct integers and L2 contains all distinct integers, but there can be many elements common between L1 and L2.
Returned list contains all elements that are common to L1 and L2. The elements in the returned list can be in any order.
For example.

if L1 = [5, 8, 2] and L2 = [6, 8, 1] then, findCommonElements(L1, L2) should return list [8].

if L1 = [3, 7, 2, 9, 5] and L2 = [6, 3, 7, 5, 4] then, findCommonElements(L1, L2) should return list [3, 7, 5].


Do not use Python set built-in function


Sample input

[23, 24, 18, 22, 20, 10, 17, 12, 16, 19, 21, 15, 14, 11, 13]
[23, 22, 33, 24, 31, 21, 20, 26, 30, 29, 25, 27, 28, 34, 32]
Output

[20, 21, 22, 23, 24]
Sample input 2

[3, 7, 2, 9, 5]
[6, 3, 7, 5, 4]
Output

[3, 5, 7]
'''

def findCommonElements(l1,l2):
    l1.sort()
    l2.sort()
    
    i,j = 0,0
    result = []
    
    while i < len(l1) and j < len(l2):
        if l1[i] == l2[j]:
            result.append(l1[i])
            i += 1
            j += 1
        
        elif l1[i] > l2[j]:
            j += 1
        
        else:
            i += 1
    
    return result            