from collections import deque

def bfs():
    while q_f:
        x,y = q_f.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < r and 0<= ny < r:
                if not visited_f[nx][ny] and graph[nx][ny] != '#':
                    visited_f[nx][ny] = visited_f[x][y] + 1
                    q_f.append((nx,ny))
    while q_j:
        x,y = q_j.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0<= nx < r and 0<= ny < c:
                if graph[nx][ny] != '#' and not visited_j[nx][ny]:
                    if not visited_f[nx][ny] or visited_f[nx][ny] > visited_j[x][y] + 1:
                        visited_j[nx][ny] = visited_j[x][y] + 1
                        q_j.append((nx,ny))
            else:
                return visited_j[x][y]
    return 'IMPOSSIBLE'

dx = [1,0,-1,0]
dy = [0,1,0,-1]

r,c = map(int,input().split())
graph = []

q_j = deque()
q_f = deque()

visited_j = [[0] * c for _ in range(r)]
visited_f = [[0] * c for _ in range(r)]


for i in range(r):
    temp = list(input())
    for j in range(len(temp)):
        if temp[j] == 'J':
            q_j.append((i,j))
            visited_j[i][j] = 1
        elif temp[j] == 'F':
            q_f.append((i,j))
            visited_f[i][j] = 1
    graph.append(temp)

print(bfs())
