n = int(input())
n_list = list(map(int,input().split()))

def revers(x):
    res =0
    while x>0:
        t=x%10
        res = res*10+t
        x=x//10
    return res

def isPrime(x):
    if x == 1:
        return False
    for i in range(2, x):
        if x %i == 0:
            return False
    return True

for i in n_list:
    tmp = revers(i)
    if isPrime(tmp):
        print(tmp, end=" ")
