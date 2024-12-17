from collections import deque
dx = [-1,0,1,0]
dy = [0,1,0,-1]
n = int(input())
board = [list(map(int,input())) for _ in range(n)]
cnt = 0
res =[]
Q=deque()
for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            board[i][j] = 0
            Q.append((i,j))
            cnt +=1
            while Q:
                tmp=Q.popleft()
                for k in range(4):
                    x = tmp[0]+dx[k]
                    y = tmp[0]+dy[k]
                    if x<0 or x>=n or y<0 or y>=n or board[x][y] == 0:
                        continue 