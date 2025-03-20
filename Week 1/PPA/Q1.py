'''
Twin primes are pairs of prime numbers that differ by 2. For example (3, 5), (5, 7), and (11,13) are twin primes.
Write a function Twin_Primes(n, m) where n and m are positive integers and n < m , that returns all unique twin primes between m and n (both inclusive). 
The function returns a list of tuples and each tuple (a,b) represents one unique twin prime where n <= a < b <= m.
'''

def check_prime(num):
    if num == 1:
        return False
    i = 2
    while i*i <= num:
        if num%i == 0:
            return False
        i += 1
    return True
    
def Twin_Primes(n,m):
    lst = []
    for num in range(n,m+1):
        if check_prime(num) == True:
            lst.append(num)
    result = []
    for j in range(len(lst)-1):
        if lst[j+1] - lst[j] == 2:
            result.append((lst[j],lst[j+1]))
    return result


n=int(input())
m=int(input())
print(sorted(Twin_Primes(n, m)))