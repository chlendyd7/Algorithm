# import os
# import sys


# BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # 현재 실행 중인 파일의 절대 경로
# sys.stdin = open(os.path.join(BASE_DIR, 'input.txt'), 'r')

from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N, M = map(int, input().split())
board = [list(input().strip()) for _ in range(N)]

# 초기 위치
red, blue = None, None
for i in range(N):
    for j in range(M):
        if board[i][j] == 'R':
            red = (i, j)
        elif board[i][j] == 'B':
            blue = (i, j)

def move(x, y, dx, dy):
    cnt = 0
    while board[x+dx][y+dy] != '#' and board[x][y] != 'O':
        x += dx
        y += dy
        cnt += 1
    return x, y, cnt

def bfs():
    visited = set()
    q = deque()
    q.append((0, *red, *blue))
    visited.add((*red, *blue))

    while q:
        depth, rx, ry, bx, by = q.popleft()
        if depth >= 10:
            return -1
        for i in range(4):
            nrx, nry, rcnt = move(rx, ry, dx[i], dy[i])
            nbx, nby, bcnt = move(bx, by, dx[i], dy[i])

            if board[nbx][nby] == 'O':
                continue
            if board[nrx][nry] == 'O':
                return depth + 1

            if nrx == nbx and nry == nby:
                if rcnt > bcnt:
                    nrx -= dx[i]
                    nry -= dy[i]
                else:
                    nbx -= dx[i]
                    nby -= dy[i]

            if (nrx, nry, nbx, nby) not in visited:
                visited.add((nrx, nry, nbx, nby))
                q.append((depth + 1, nrx, nry, nbx, nby))

    return -1

print(bfs())
