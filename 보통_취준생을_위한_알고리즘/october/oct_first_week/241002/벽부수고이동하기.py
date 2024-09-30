from collections import deque
dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]
def check(row, col):
    return row < 0 or row >=N or col < 0 or col >=M

def bfs():
    visited = [[[0]*2 for _ in range(M)] for _ in range(N)]
    visited[0][0][0] = 1
    while q:
        x,y,wall = q.popleft()
        if x == N -1 and y == M -1:
            return visited[x][y][wall]
        for k in range(4):
            xx = x + dx[k]
            yy = y + dy[k]
            if 0<= xx < N and 0<= yy < M and visited[xx][yy][wall] == 0:
                if board[xx][yy] == 0:
                    visited[xx][yy][wall] = visited[x][y][wall] + 1
                    q.append([xx, yy, wall])
                if wall == 0 and board[xx][yy] == 1:
                    visited[xx][yy][1] = visited[x][y][0] + 1
                    q.append([xx,yy,1])
    return -1        


N,M = map(int,input().split())
q = deque()
q.append([0,0,0])
board = [list(map(int,input())) for _ in range(N)]
print(bfs())
