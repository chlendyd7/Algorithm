n,k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
dp = [1e9] * 10001
dp[0] = 0
for coin in coins:
    for i in range(coin, k+1):
        # if i % coin == 0:
        #     dp[i] = i%coin
        # else:
            dp[i] = min(dp[i], dp[i-coin]+1)

print(dp[k])
