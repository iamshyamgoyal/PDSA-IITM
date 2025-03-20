'''
Write a function Findpeak(L) that accepts a list L of n distinct elements and returns the peak element of the list. A list element is a peak if it is greater than its neighbors. For corner elements, we need to consider only one neighbor. Write an efficient solution of O(logn) complexity. Consider that there is only one peak is in the list, L.


Sample Input 1

[5, 10, 20, 15]
Output

20

Sample Input 2

[1,2,3,4,5,6,7,8]
Output

8
'''

def Findpeak(lst):
    low = 0
    high = len(lst)-1
    
    while high >= low:
        mid = ( low + high ) // 2
        
        if (mid == len(lst)-1 or lst[mid] >= lst[mid+1]) and  (mid == 0 or lst[mid] >= lst[mid-1]):
            return lst[mid]
            
        elif mid > 0 and lst[mid] < lst[mid-1]:
            high = mid - 1
        else:
            low = mid + 1