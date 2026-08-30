# https://atcoder.jp/contests/dp/tasks/dp_a

n = int(input())
dp = [1e9] * n
stones = list(map(int, input().split()))

dp[0] = 0
dp[1] = abs(stones[0] - stones[1])
for i in range(1, n):
    dp[i] = min(
        dp[i-1] + abs(stones[i] - stones[i-1]),
        dp[i-2] + abs(stones[i] - stones[i-2])
        )
print(dp[n-1])