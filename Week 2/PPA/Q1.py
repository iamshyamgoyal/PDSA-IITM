def binarySearchIndexAndComparisons(L,K):
    cnt = 0
    left, right = 0, len(L)-1
    present = False
    while left <= right:
        mid = (left + right) // 2
        cnt += 1
        
        if L[mid] == K:
            present = True
            break
        elif L[mid] < K:
            left = mid + 1
        else:
            right = mid -1
        
            
    return (present, cnt)