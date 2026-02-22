
def combination(k, coins):
    dp = [0] * (k+1)
    dp[0] = 1
    for coin in coins:
        for i in range(coin, k+1):
            dp[i] += dp[i - coin]
    return dp[k]


n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

print(combination(k,coins))