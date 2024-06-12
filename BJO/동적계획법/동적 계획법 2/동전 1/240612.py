def coin_combinations(n, k, coins):
    dp = [0] * (k +1)
    dp[0] = 1
    
    for coin in coins:
        for j in range(coin, k+1):
            
for _ in range(n):
    coins.append(int(input()))

def dfs(result):
    if result == k:
        return 1

    if dp[result] != -1:
        return dp[result]
    
    for coin in coins:
        if result + coin <= k:
            dp[result] += dfs(result + coin)
    return dp[result]

dp = [-1 for _ in range(k)]

n,k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
print(dfs(0))


def coin_combinations(n, k, coins):
    dp = [0] * (k + 1)
    dp[0] = 1  # 기본 값 초기화

    for coin in coins:
        for j in range(coin, k + 1):
            dp[j] += dp[j - coin]

    return dp[k]

# 입력 받기
n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

# 경우의 수 출력
print(coin_combinations(n, k, coins))