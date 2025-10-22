from collections import deque
import heapq
import sys


dx = [1,0,-1,0]
dy = [0,1,0,-1]

r,c = map(int,input().split())
board = [list(input()) for _ in range(c)]
fire_v = [[0] * c for _ in range(r)]
jihon_v = [[0] * c for _ in range(r)]

fire_q = deque()
jihon_q = deque()

for i in range(r):
    for j in range(c):
        if board[i][j] == 'J':
            jihon_q.append([i,j])
            jihon_v[i][j] = 1
        elif board[i][j] == 'F':
            fire_q.append([i,j])
            fire_v[i][j] = 1

while fire_q:
    x,y = fire_q.popleft()
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0<= nx < r and 0<= ny < c \
            and board[nx][ny] != '#' and fire_v[nx][ny] == 0:
            fire_v[nx][ny] = fire_v[x][y] + 1
            fire_q.append((nx,ny))

while jihon_q:
    x,y = jihon_q.popleft()

    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0<= nx < r and 0<= ny < c:
            if board[nx][ny] != '#' and not jihon_v[nx][ny]:
                if not fire_v[nx][ny] or fire_v[nx][ny] > jihon_v[x][y] + 1:
                    jihon_v[nx][ny] = jihon_v[x][y] + 1
                    jihon_q.append((nx,ny))
        
        else:
            print(jihon_v[x][y])
            sys.exit()

print('IMPOSSIBLE')