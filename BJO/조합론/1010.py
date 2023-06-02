def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)


t = int(input())
ans = 0
for i in range(t):
    n,m = list(map(int,input().split()))
    ans = factorial(m)//(factorial(n)*factorial(m-n))
    print(ans)