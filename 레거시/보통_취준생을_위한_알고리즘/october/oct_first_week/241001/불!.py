from collections import deque
import sys

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

r,c = map(int,input().split())
board = []

q_fire = deque()
q_jihon = deque()

visited_fire = [[0]* c for _ in range(r)]
visited_jihon = [[0]* c for _ in range(r)]

for i in range(r):
    temp = list(input())
    for j in range(c):
        if temp[j] == 'F':
            q_fire.append([i,j,1])
            visited_fire[i][j] = 1
        elif temp[j] == 'J':
            q_jihon.append([i,j,1])
            visited_jihon[i][j] = 1
    board.append(temp)


while q_fire:
    x,y,time = q_fire.popleft()
    
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0<= nx < r and 0<= ny < c:
            if board[nx][ny] != '#' and not visited_fire[nx][ny]:
                visited_fire[nx][ny] = time + 1
                q_fire.append([nx,ny,time+1])

while q_jihon:
    x,y,time = q_jihon.popleft()

    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0<= nx < r and 0<= ny < c:
            if board[nx][ny] != '#' and not visited_jihon[nx][ny]:
                if visited_fire[nx][ny] == 0 or  visited_fire[nx][ny] > time+1:
                    visited_jihon[nx][ny] = time + 1
                    q_jihon.append([nx,ny,time+1])
        else:
            print(visited_jihon[x][y])
            sys.exit()

print("IMPOSSIBLE")


