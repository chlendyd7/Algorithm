k, n = map(int, input().split())
max_height = k + n
dp = [[0] * (max_height + 2) for _ in range(n+1)]

dp[0][k] = 1
for t in range(1, n+1):
    for h in range(1, max_height+1):
        dp[t][h] = dp[t-1][h-1] + dp[t-1][h+1]

print(sum(dp[n]))
