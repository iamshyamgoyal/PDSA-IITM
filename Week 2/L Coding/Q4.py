'''
Given a list L of random numbers and another number pairSum, find whether there exists two numbers in the list such that their sum is equal to pairSum.

Write a Python function findPair(L, pairSum) that return True if there exist a pair of integers in L whose sum is equal to x, False otherwise. Try to write a solution which is O(nlogn) or better.


Hint: Try to sort the list first.

 

For example, consider the below list. We need to find if there exists any pair whose sum is equal to 21. 11+10 = 21. So the function should return True.

For the same list, if we want to find if there exist any pair whose sum is equal to 2. Clearly there is no such pair, so the function should return False.


Sample Input 1

10 4 11 5 1 8 7
21
Output

True
Sample Input 2

10 4 11 5 1 8 7
2
Output

False
'''


def findPair(lst, psum):
    def divide_sort(lst1):
        if len(lst1) <= 1:
            return lst1
        
        mid  = len(lst1) // 2
        left = divide_sort(lst1[:mid])
        right = divide_sort(lst1[mid:])
        
        return merge(left, right)
    
    def merge(left, right):
        sorted_lst = []
        
        i,j = 0,0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                sorted_lst.append(left[i])
                i += 1
            
            else:
                sorted_lst.append(right[j])
                j += 1
            
        sorted_lst.extend(left[i:])
        sorted_lst.extend(right[j:])
        
        return sorted_lst
    
    slst = divide_sort(lst)
    i = 0
    j = len(slst) - 1
    while i < j:
        nsum = slst[i] + slst[j]
        if nsum == psum:
            return True
        elif nsum < psum:
            i += 1
        else:
            j -= 1
    
    return False


L = [int(item) for item in input().split()]
pairsum = int(input())
print(findPair(L, pairsum))