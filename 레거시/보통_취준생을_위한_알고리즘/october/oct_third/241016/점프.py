from collections import deque


n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]


dp = [[0] * n for _ in range(n)]
dp[0][0] = 1

for i in range(n):
    for j in range(n):
        k = graph[i][j]

        if k == 0 or dp[i][j] == 0:
            continue
        if i + k < n:
            dp[i+k][j] += dp[i][j]
        if j + k < n:
            dp[i][j+k] += dp[i][j]
print(dp[n-1][n-1])
