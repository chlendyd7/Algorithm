# https://atcoder.jp/contests/dp/tasks/dp_b

n, k = map(int, input().split())
stones = list(map(int, input().split()))
dp = [1e9] * n
dp[0] = 0

for i in range(1, n):
    for j in range(1,k+1):
        if i-j >= 0:
            dp[i] = min(dp[i], dp[i-j] + abs(stones[i] - stones[i-j]))

print(dp[n-1])