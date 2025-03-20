def histogram(lst):
    h = {}
    for i in lst:
        if i not in h:
            h[i] = 1
        else:
            h[i] += 1
    
    result = []
    for k,v in h.items():
        result.append((k,v))
        
    result = sorted(result, key=lambda x: (x[1], x[0]))
    return result
    
L=eval(input())
print(histogram(L))