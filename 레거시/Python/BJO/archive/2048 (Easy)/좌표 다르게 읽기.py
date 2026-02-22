UP = "UP"
DOWN = "DOWN"
LEFT = "LEFT"
RIGHT = "RIGHT"

def move(board, dir):
    N = len(board)
    new_board = [[0] * N for _ in range(N)]

    for r in range(N):
        for c in range(N):
            if dir == UP:
                nr, nc = r, c
            elif dir == DOWN:
                nr, nc = N-1-r, c
            elif dir == LEFT:
                nr, nc = r, c
            elif dir == 3:
                nr, nc = r, N-1-c

            new_board[nr][nc] = board[r][c]

    return new_board
