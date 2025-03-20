'''
Note:- In function, no need to return any list, just sort input list `L` in place.
'''

def sortInRange(L, r):
    count = [0] * (r + 1)

    for num in L:
        count[num] += 1

    index = 0
    for i in range(r + 1):
        for _ in range(count[i]):
            L[index] = i
            index += 1
