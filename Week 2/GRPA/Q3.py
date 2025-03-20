''''
Note:- Your function should not return any list and should only merge the given sorted lists inplace.
'''

def mergeInPlace(A, B):
    
    for i in range(len(A)):
        if A[i] > B[0]:
            A.swap(i, B, 0)
            
            j = 0
            while j < len(B) - 1 and B[j] > B[j + 1]:
                B.swap(j, B, j + 1)
                j += 1
