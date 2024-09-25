from collections import deque

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

def bfs():
    visit = [[[0]*2 for _ in range(M)] for _ in range(N)]
    visit[0][0][0] = 1
    while q:
        x,y, wall = q.popleft()
        if x == N-1 and y == M-1:
            return visit[x][y][wall]
        for k in range(4):
            xx = x + dx[k]
            yy = y + dy[k]
            if 0<= xx < N and 0<= yy < M and visit[xx][yy][wall] == 0:
                if maze[xx][yy] == 0:
                    visit[xx][yy][wall] = visit[x][y][wall] + 1
                    q.append([xx, yy, wall])
                if wall == 0 and maze[xx][yy] == 1:
                    visit[xx][yy][1] = visit[x][y][0] + 1
                    q.append([xx,yy,1])
    return -1

N, M = map(int,input().split())
maze = [list(map(int,input())) for _ in range(N)]
q = deque()
q.append([0,0,0])
print(bfs())