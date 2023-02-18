n = int(input())
coin = list(map(int,input().split()))
m = int(input())

dp = [10001] * (m+1)
dp[0] = 0

for i in range(n):
    for j in range(coin[i], m+1):
        dp[j] = min(dp[j], dp[j - coin[i]]+1)
print(dp[m])