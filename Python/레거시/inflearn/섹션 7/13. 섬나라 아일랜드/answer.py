import sys
from collections import deque
# sys.stdin=open("input.txt", "r")
dx=[-1, -1, 0, 1, 1, 1, 0, -1] # 8방향 대각선 포함 탐색법 3,3좌표로 생각해볼 것
dy=[0, 1, 1, 1, 0, -1, -1, -1] # 시계방향 왼쪽 아래부터 좌표가 시작되나?

n=int(input())
board=[list(map(int, input().split())) for _ in range(n)]
cnt=0
Q=deque()
for i in range(n):
    for j in range(n):
        if board[i][j]==1: # 8방향 돌기
            board[i][j]=0
            Q.append((i, j)) # 좌표 넣고
            while Q: # 
                tmp=Q.popleft() # 좌표 하나 나옴 살짝 이해 안됨 다시 보기
                for k in range(8): # 8방향 돌기
                    x=tmp[0]+dx[k]
                    y=tmp[1]+dy[k]
                    if 0<=x<n and 0<=y<n and board[x][y]==1:
                        board[x][y]=0 # 이제 방문할 예정
                        Q.append((x, y)) # 이건 어떤 용도?
            cnt+=1 # 돌고 끝나면 cnt+1
print(cnt)
