n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
dp = [[[0]*3 for _ in range(n+1)] for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, n+1):
        now = board[i-1][j-1]
        prev_up = dp[i-1][j]
        prev_left = dp[i][j-1]

        for k in range(3):
            dp[i][j][k] = max(prev_left[k], prev_up[k])

        if now == 0:
            dp[i][j][0] = max(dp[i][j][0], max(prev_left[2], prev_up[2]) + 1)
            if dp[i][j][0] == 0:
                dp[i][j][0] = 1
        elif now == 1:
            if max(prev_left[0], prev_up[0]) > 0:
                dp[i][j][1] = max(dp[i][j][1], max(prev_left[0], prev_up[0]) + 1)
        elif now == 2:
            if max(prev_up[1], prev_left[1]) > 0:
                dp[i][j][2] = max(dp[i][j][2], max(prev_left[1], prev_up[1]) + 1)

print(max(dp[n][n]))
