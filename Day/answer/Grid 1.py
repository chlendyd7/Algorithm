h,w = map(int, input().split())
board = [list(input()) for _ in range(h)]

dp = [[0] * (w+1) for _ in range(h+1)]
dp[1][1] = 1
for i in range(1, h+1):
    for j in range(1, w+1):
        if i==1 and j == 1:
            continue
        if board[i-1][j-1] == '#':
            continue
        dp[i][j] = ((dp[i-1][j] + dp[i][j-1]) % (10**9 + 7))

print(dp[h][w])
