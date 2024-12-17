import sys
input = sys.stdin.readline

n = int(input().strip())

matrices = []
for _ in range(n):
    r, c = map(int, input().split())
    matrices.append((r, c))

dp = [[0] * n for _ in range(n)]

for length in range(1, n):
    for i in range(n - length):
        j = i + length
        dp[i][j] = float('inf')

        for k in range(i, j):
            cost = dp[i][k] + dp[k + 1][j] + matrices[i][0] * matrices[k][1] * matrices[j][1]
            if cost < dp[i][j]:
                dp[i][j] = cost

print(dp[0][n - 1])
