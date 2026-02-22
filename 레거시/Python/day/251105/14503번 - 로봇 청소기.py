dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

N, M = map(int, input().split())
r,c,d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

x, y = r, c
cnt = 0
while True:
    if board[r][c] == 0:
        board[r][c] = 2
        cnt += 1
    moved = False
    for i in range(4):
        d = (d+3) % 4
        nx, ny = r + dx[d], c + dy[d]
        if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == 0:
            r, c = nx, ny
            moved = True
            break
    if moved:
        continue

    bx, by = r - dx[d], c - dy[d]
    if not (0 <= bx < N and 0 <= by < M) or board[bx][by] == 1:
        break
    r, c = bx, by

print(cnt)
