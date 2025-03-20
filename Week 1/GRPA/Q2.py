def prime_list(num):
    lst = []
    for j in range(2,num):
        i = 2
        flag = True
        while i*i <= j:
            if j % i == 0:
                flag = False
                break
            i += 1
        if flag == True:
            lst.append(j)
    
    return lst
    
    
    
def Goldbach(num):
    lst = prime_list(num)
    result = []
    
    for n1 in lst:
        if num - n1 in lst:
            result.append((min(n1, num - n1), max(n1, num - n1)))
            lst.remove(n1)
            if n1 != num - n1:
                lst.remove(num - n1)

    return result
    
n=int(input())
print(sorted(Goldbach(n)))