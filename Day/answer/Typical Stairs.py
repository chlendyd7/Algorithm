n,m = map(int, input().split())
stairs = [int(input()) for _ in range(m)]
print(stairs)

dp = [0] * (n+1)
dp[1] = 1
dp[2] = 2

for i in range(3, n+1):
    if i not in stairs:
        dp[i] = dp[i-2] + dp[i-1] + 2

print(dp[n])
