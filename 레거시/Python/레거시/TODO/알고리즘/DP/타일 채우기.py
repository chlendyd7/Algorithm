# https://velog.io/@yje876/python%EB%B0%B1%EC%A4%80DP-2133-%ED%83%80%EC%9D%BC-%EC%B1%84%EC%9A%B0%EA%B8%B0

n = int(input())

dp = [0]*(n+1)

dp[0] = 1

if n  >= 2:
    dp[2] = 3

for i in range(4,n+1,2):
    dp[i] = dp[i-2] *dp[2]
    for j in range(0,i-2, 2):
        dp[i] += dp[j]*2

print(dp[n])