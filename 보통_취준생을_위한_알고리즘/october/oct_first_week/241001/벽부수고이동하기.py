from collections import deque
import sys

dx = [1,0,-1,0]
dy = [0,1,0,-1]

n,m = map(int,input().split())
board = [list(map(int,input())) for _ in range(n)]
visited = [[[0]*2 for _ in range(m)] for _ in range(n)]

q = deque()
q.append([0,0,0])
visited[0][0][0] = 1

while q:
    x,y, wall = q.popleft()
    if x == n-1 and y == m -1:
        print(visited[x][y][wall])
        sys.exit()
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0<= nx < n and 0<= ny < m and not visited[nx][ny][wall]:
            if board[nx][ny] == 0:
                visited[nx][ny][wall] = visited[x][y][wall] + 1
                q.append([nx,ny,wall])
            if board[nx][ny] == 1 and not wall:
                visited[nx][ny][1] = visited[x][y][0] + 1
                q.append([nx,ny,1])
print(-1)
