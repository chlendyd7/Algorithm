t = int(input())
dp = [1]* 10001
ls = [int(input()) for _ in range(t)]

for i in range(2, 10001):
    dp[i] += dp[i -2]
for i in range(3, 10001):
    dp[i] += dp[i-3]

for num in ls:
    print(dp[num])
