n = int(input())
dp = [0] * 1001
ls = list(map(int,input().split()))
ls.insert(0,0)

answer = 0
for i in range(1, n+1):
    for j in range(0, i):
        if ls[i] > ls[j]:
            dp[i] = max(dp[j]+1, dp[i])

print(max(dp))
