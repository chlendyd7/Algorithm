n = int(input())
stones = list(map(int, input().split()))

dp = [10**18] * (n+1)
dp[0] = 0
dp[1] = abs(stones[0] - stones[1])

for i in range(2, n):
    dp[i] = min(dp[i-2] + abs(stones[i-2] - stones[i]), dp[i-1] + abs(stones[i-1] - stones[i]))

print(dp[n-1])

