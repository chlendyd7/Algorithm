import sys
input = sys.stdin.readline

T = int(input())

prime = [True for _ in range(1000001)]


for i in range(2, 1000001):
    if prime[i]:
        prime.append(i)
        for j in range(2*i, 1000001, i):
            prime[j] = False

for _ in range(T):
    result = 0
    n = int(input())

    for i in range(2,n//2+1): 
        # 동일한 조합이 나올 수 있으므로
        if prime[i] and prime[n-i]:
            result += 1
    print(result)

