# dp[모양][행][열]
N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
dp = [[[0] * N for _ in range(N)] for _ in range(3)]
RIGHT, DOWN, DAGAK = 0, 1, 2
dp[RIGHT][0][1] = 1

for r in range(N):
    for c in range(N):
        # 1. 가로 상태에서 전개
        if dp[RIGHT][r][c] > 0:
            if c + 1 < N and board[r][c+1] == 0:
                dp[RIGHT][r][c+1] += dp[RIGHT][r][c]
                if r + 1 < N and board[r+1][c] == 0 and board[r+1][c+1] == 0:
                    dp[DAGAK][r+1][c+1] += dp[RIGHT][r][c]

        # 2. 세로 상태에서 전개
        if dp[DOWN][r][c] > 0:
            if r + 1 < N and board[r+1][c] == 0:
                dp[DOWN][r+1][c] += dp[DOWN][r][c]
                if c + 1 < N and board[r][c+1] == 0 and board[r+1][c+1] == 0:
                    dp[DAGAK][r+1][c+1] += dp[DOWN][r][c]

        # 3. 대각선 상태에서 전개
        if dp[DAGAK][r][c] > 0:
            # 가로로
            if c + 1 < N and board[r][c+1] == 0:
                dp[RIGHT][r][c+1] += dp[DAGAK][r][c]
            # 세로로
            if r + 1 < N and board[r+1][c] == 0:
                dp[DOWN][r+1][c] += dp[DAGAK][r][c]
            # 대각선으로
            if r + 1 < N and c + 1 < N and \
            board[r+1][c] == 0 and board[r][c+1] == 0 and board[r+1][c+1] == 0:
                dp[DAGAK][r+1][c+1] += dp[DAGAK][r][c]

print(sum(dp[s][N-1][N-1] for s in range(3)))
