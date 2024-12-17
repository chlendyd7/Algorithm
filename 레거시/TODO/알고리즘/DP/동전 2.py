n,k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
dp = [1e9] * 10001
dp[0] = 0
for coin in coins:
    for j in range(coin, k + 1):
        dp[j] = min(dp[j], dp[j - coin] + 1)

if dp[k]== 1e9:
    print(-1)
else:
    print(dp[k])
