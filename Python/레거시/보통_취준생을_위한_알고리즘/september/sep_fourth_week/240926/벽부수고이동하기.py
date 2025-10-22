from collections import deque


dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

def bfs():
    visited = [[[0]*2 for _ in range(m)]for _ in range(n)]
    visited[0][0][0] = 1
    while q:
        x,y,wall = q.popleft()
        if x == n-1 and y == m-1:
            return visited[x][y][wall]
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0<= nx < n and 0<= ny <m and visited[nx][ny][wall] == 0:
                if board[nx][ny] == 0:
                    visited[nx][ny][wall] = visited[x][y][wall] + 1
                    q.append([nx,ny,wall])
                if wall == 0 and board[nx][ny] == 1:
                    visited[nx][ny][1] = visited[x][y][0] + 1
                    q.append([nx,ny,1])
    return -1

n,m = map(int,input().split())
board = [list(map(int,input())) for _ in range(n)]
q = deque()
q.append([0,0,0])

print(bfs())