n, k = map(int, input().split())
stones = list(map(int, input().split()))
dp = [1e9] * n
dp[0] = 0

for i in range(n):
    for j in range(1, k+1):
        if i+j < n:
            dp[i+j] = min(dp[i+j], dp[i]+ abs(stones[i] - stones[i+j]))

print(dp[n-1])
