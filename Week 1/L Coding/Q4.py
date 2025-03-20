def expanding(lst):
    n = -1
    for i in range(len(lst)-1):
        if abs(lst[i] - lst[i+1]) > n:
            n = abs(lst[i] - lst[i+1])
        else:
            return False
    return True



L = eval(input())
print(expanding(L))