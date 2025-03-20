'''
Write a function shuffle(l1,l2) that takes two lists, l1 and l2 as input, and returns a list consisting of the first element in l1, then the first element in l2, then the second element in l1, then the second element in l2, and so on. If the two lists are not of equal length, the remaining elements of the longer list are appended at the end of the shuffled output.


Sample Input

[0,2,4]
[1,3,5]
Output

[0, 1, 2, 3, 4, 5]
Sample Input

[0,2,4]
[1]
Output

[0, 1, 2, 4]
'''

def shuffle(l1, l2):
    n1 = len(l1)
    n2 = len(l2)
    
    new_lst = []
    for i in range(min(n1,n2)):
        new_lst.append(l1[i])
        new_lst.append(l2[i])
    
    if n1 < n2:
        for j in range(i+1,n2):
            new_lst.append(l2[j])
    
    if n2 < n1:
        for j in range(i+1,n1):
            new_lst.append(l1[j])
    
    return new_lst

L1 = eval(input())
L2 = eval(input())
print(shuffle(L1,L2))