from collections import deque
import heapq

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def bfs():
    visited = [[[0]*2 for _ in range(M)] for _ in range(N)]
    q = deque()
    q.append([0,0,0])
    visited[0][0][0] = 1
    while q:
        x, y, wall = q.popleft()
        if x == N-1 and y == M-1:
            return visited[x][y][wall]
        
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0<= nx < N and 0<= ny < M and not visited[nx][ny][wall]:
                if board[nx][ny] == 0:
                    visited[nx][ny][wall] = visited[x][y][wall] + 1
                    q.append([nx,ny,wall])
                elif board[nx][ny] == 1 and not wall:
                    visited[nx][ny][1] = visited[x][y][0] + 1
                    q.append([nx,ny,1])
    return  -1



N,M = map(int,input().split())
board = [list(map(int,input())) for _ in range(N)]
print(bfs())