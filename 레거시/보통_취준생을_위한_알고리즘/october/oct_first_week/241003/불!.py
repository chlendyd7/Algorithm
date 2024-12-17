from collections import deque


dx = [1,0,-1,0]
dy = [0,1,0,-1]

def check(row, col):
    return 0<= row < R and 0<= col < C

def bfs():

    while q_fire:
        x, y = q_fire.popleft()
        
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if check(nx, ny) and not visited_f[nx][ny] and board[nx][ny] != '#':
                visited_f[nx][ny] = visited_f[x][y] + 1
                q_fire.append([nx,ny])
    
    while q_jihon:
        x, y = q_jihon.popleft()

        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if check(nx, ny):
                if not visited_j[nx][ny] and board[nx][ny] != '#':
                    if not visited_f[nx][ny] or visited_f[nx][ny] > visited_j[x][y] + 1:
                        visited_j[nx][ny] = visited_j[x][y] + 1
                        q_jihon.append([nx,ny])

            else: 
                return visited_j[x][y]

    return "IMPOSSIBLE"


R,C = map(int,input().split())
board = []
q_fire = deque()
q_jihon = deque()

visited_f = [[False] * C for _ in range(R)]
visited_j = [[False] * C for _ in range(R)]

for i in range(R):
    temp = list(input())
    for j in range(C):
        if temp[j] == 'J':
            q_jihon.append([i,j])
            visited_j[i][j] = 1
        elif temp[j] == 'F':
            q_fire.append([i,j])
            visited_f[i][j] = 1
    board.append(temp)

print(bfs())
