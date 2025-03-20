def check_prime(num):
    if num <= 1:
        return False
    i = 2
    while i * i <= num:
        if num % i == 0:
            return False
        i += 1
    return True

def prime_product(m):
    for i in range(2,m):
        if m%i == 0:
            if check_prime(i) == True and check_prime(m//i) == True:
                return True
        
    return False
            

n = int(input())
print(prime_product(n))