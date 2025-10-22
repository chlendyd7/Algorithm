n = int(input())
dp = [0] * (n+1)
wins = [int(input()) for _ in range(n)]
dp[0] = wins[0]
dp[1] = wins[1] + wins[0]
for i in range(3, n):
    dp[i] = max(dp[i-1], wins[i] + dp[i-2], wins[i] + dp[i-3] + wins[i-1])

print(dp[n-1])
