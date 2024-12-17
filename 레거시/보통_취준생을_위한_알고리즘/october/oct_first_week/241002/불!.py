from collections import deque

def check(col, row):
    return 0 <= col < r and 0<= row < c

def bfs():
    visited_f = [[0] * c for _ in range(r)]
    visited_j = [[0] * c for _ in range(r)]

    for i in range(c):
        for j in range(r):
            if board[i][j] == 'F':
                q_fire.append([i,j])
                visited_f[i][j] = 1
            elif board[i][j] == 'J':
                q_jihon.append([i,j])
                visited_j[i][j] = 1

    while q_fire:
        x,y = q_fire.popleft()
        
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if check(nx, ny):
                if board[nx][ny] != '#' and visited_f[nx][ny] == 0:
                    visited_f[nx][ny] = visited_f[x][y] + 1
                    q_fire.append([nx,ny])
    
    while q_jihon:
        x,y = q_jihon.popleft()
        
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if check(nx, ny):
                if board[nx][ny] != '#' and visited_j[nx][ny] == 0:
                    if visited_f[nx][ny] == 0 or visited_f[nx][ny] > visited_j[x][y] + 1:
                        visited_j[nx][ny] = visited_j[x][y] + 1
                        q_jihon.append([nx, ny])
            else:
                return visited_j[x][y]

    return "IMPOSSIBLE"

dx = [1,0,-1,0]
dy = [0,1,0,-1]

r,c = map(int,input().split())
board = [list(input()) for _ in range(r)]

q_fire = deque()
q_jihon = deque()
print(bfs())
