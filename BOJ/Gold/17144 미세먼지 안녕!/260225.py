R, C, T = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(R)]

r1 = 0
for r in range(R):
    if board[r][0] == -1:
        r1 = r
        r2 = r+1
        break

def mise_spread(board):
    new_board = [[0] * C for _ in range(R)]
    new_board[r1][0] = -1
    new_board[r2][0] = -1
    for r in range(R):
        for c in range(C):
            if board[r][c] > 4:
                cnt = 0
                for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < R and 0 <= nc < C and board[nr][nc] != -1:
                        cnt += 1
                        new_board[nr][nc] += board[r][c] // 5
                new_board[r][c] += board[r][c] - (board[r][c] // 5) * cnt
    return new_board

def cleanup(board):
    for i in range(r1-1, 0, -1):
        board[i][0] = board[i-1][0]
    for i in range(C-1):
        board[0][i] = board[0][i+1]
    for i in range(r1+1):
        board[i][C-1] = board[i+1][C-1]
    for i in range(C-1, 0, -1):
        board[r1][i] = board[r1][i-1]
    board[r1][1] = 0

    for i in range(r2+1, R-1):
        board[i][0] = board[i+1][0]
    for i in range(C-1):
        board[R-1][i] = board[R-1][i+1]
    for i in range(R-1, r2, -1):
        board[i][C-1] = board[i-1][C-1]
    for i in range(C-1, 1, -1):
        board[r2][i] = board[r2][i-1]
    board[r2][1] = 0

for t in range(T):
    board = mise_spread(board)
    # print(board)
    cleanup(board)
    print(board)
