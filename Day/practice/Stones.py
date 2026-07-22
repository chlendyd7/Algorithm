n, k = map(int, input().split())
A = list(map(int, input().split()))

dp = [False] * (k+1)
dp[0] = False

for i in range(1, k+1):
    for x in A:
        if i >= x and not dp[i-x]:
            dp[i] = True
            break
