def odd_one(lst):
    h = {}
    
    for i in lst:
        if type(i) in h:
            h[type(i)] += 1
        else:
            h[type(i)] = 1
    
    for key,value in h.items():
        if value == 1:
            return key.__name__


print(odd_one(eval(input().strip())))