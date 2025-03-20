def sumsquare(lst):
    e = 0
    o = 0
    for i in lst:
        if i%2 == 0:
            e += i**2
        else:
            o += i**2
    
    return [o, e]
    
L = eval(input())
print(sumsquare(L))