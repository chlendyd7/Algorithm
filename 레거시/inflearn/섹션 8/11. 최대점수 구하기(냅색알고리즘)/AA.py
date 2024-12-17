n ,m = map(int,input().split())
dp = [0]*(m+1)

for i in range(n):
    score, time = map(int,input().split())
    for j in range(m, time-1, -1):
        dp[j] = max(dp[j], dp[j-time]+score)

print(dp[m])