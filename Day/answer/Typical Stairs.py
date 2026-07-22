n,m = map(int, input().split())
stairs = [int(input()) for _ in range(m)]

dp = [0] * (n+1)
dp[1] = 1
dp[2] = 2

for i in range(1, n+1):
    if i not in stairs:
        dp[i] = dp[i-2] + dp[i-1]

print(dp[n] % 1000000007)
