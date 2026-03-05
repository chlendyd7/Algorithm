N = int(input())
board = [[0] * 101 for _ in range(101)]
direction = [(0,1), (-1,0), (0,-1), (1,0)]
for _ in range(N):
    x, y, d, g = map(int, input().split())
    dirs = [d]
    for _ in range(g):
        for i in range(len(dirs)-1, -1, -1):
            dirs.append((dirs[i]+1)%4)
    
    board[y][x] = 1
    for d in dirs:
        nr, nc = direction[d]
        y += nr
        x += nc
        if 0<= x <= 100 and 0 <= y <= 100:
            board[y][x] = 1

cnt = 0
for r in range(100):
    for c in range(100):
        if board[r][c] and board[r+1][c] and board[r][c+1] and board[r+1][c+1]:
            cnt += 1

print(cnt)