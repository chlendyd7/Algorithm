n = int(input())
stones = list(map(int, input().split()))
dp = [10**18] * n

dp[0] = stones[0]
dp[1] = min(abs(dp[0] - stones[1]), stones[1])
for i in range(2, n):
    dp[i] = min(abs(dp[i-2] - stones[i]), abs(stones[i-1] - stones[i]))

print(dp[n-1])
