from collections import deque
dx = [1,0,-1,0]
dy = [0,1,0,-1]

def bfs():
    while q_f:
        x,y = q_f.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < r and 0<= ny < c:
                if maze[nx][ny] !='#' and visited_f[nx][ny] == 0:
                    visited_f[nx][ny] = visited_f[x][y] + 1
                    q_f.append((nx,ny))
    
    while q_j:
        x,y = q_j.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < r and 0<= ny < c:
                if maze[nx][ny] !='#' and visited_j[nx][ny] == 0 :
                    if not visited_f[nx][ny] or visited_j[x][y] + 1 < visited_f[nx][ny]:
                        visited_j[nx][ny] = visited_j[x][y] + 1
                        q_j.append((nx,ny))

            else:
                return visited_j[x][y]
    return "IMPOSSIBLE"

q_f = deque()
q_j = deque()

r,c = map(int,input().split())
maze = [list(input()) for _ in range(r)]
visited_f = [[0] * c for _ in range(r)]
visited_j = [[0] * c for _ in range(r)]

for i in range(r):
    for j in range(c):
        if maze[i][j] == 'J':
            q_j.append((i,j))
            visited_j[i][j] = 1
        elif maze[i][j] == 'F':
            q_f.append((i,j))
            visited_f[i][j] = 1

print(bfs())
