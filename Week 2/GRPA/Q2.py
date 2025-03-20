'''
Note:- Do not use list slicing in Binary search implementation because the list slicing operation is of order O(n).
'''

def findLargest(lst):
    low = 0
    high = len(lst)-1
    
    while low <= high:
        
        if lst[low] <= lst[high]:
            return lst[high]
            
        mid = ( low + high ) // 2
        
        if (mid == 0 or lst[mid] > lst[mid-1]) and (mid == len(lst)-1 or lst[mid] > lst[mid+1]):
            return lst[mid]
            
        elif lst[mid] < lst[low]:
            high = mid - 1
        else:
            low  = mid + 1