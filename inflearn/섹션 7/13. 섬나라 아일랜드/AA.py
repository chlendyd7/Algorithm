from collections import deque
dx=[-1, -1, 0, 1, 1, 1, 0, -1] # 8방향 대각선 포함 탐색법 3,3좌표로 생각해볼 것
dy=[0, 1, 1, 1, 0, -1, -1, -1] # 시계방향 왼쪽 아래부터 좌표가 시작되나?

n=int(input())
board=[list(map(int,input().split())) for _ in range(n)]
cnt=0
res=[]
Q=deque()
for i in range(n):
    for j in range(n):
        if board[i][j]==1:
            board[i][j]=0
            Q.append((i,j))
            cnt+=1
            while Q:
                tmp=Q.popleft()
                for k in range(8):
                    x=tmp[0]+dx[k]
                    y=tmp[1]+dy[k]
                    if x<0 or x>=n or y<0 or y>=n or board[x][y]==0:
                        continue
                    board[x][y]=0
                    Q.append((x,y))
print(cnt)