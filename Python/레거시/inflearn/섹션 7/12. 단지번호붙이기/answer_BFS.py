import sys
from collections import deque
sys.stdin=open("input.txt", "r")
dx=[-1, 0, 1, 0]
dy=[0, 1, 0, -1]
n=int(input())
board=[list(map(int, input())) for _ in range(n)]
cnt=0
res=[]
Q=deque()
for i in range(n):
    for j in range(n):
        if board[i][j]==1:
            board[i][j]=0
            Q.append((i, j))
            cnt=1
            while Q:
                tmp=Q.popleft()# i,j가 pop
                for k in range(4): # 4 방향 순회
                    x=tmp[0]+dx[k]
                    y=tmp[1]+dy[k]
                    if x<0 or x>=n or y<0 or y>=n or board[x][y]==0:
                        continue # 이부분 중점으로 보기
                    board[x][y]=0 #그 방향은 0으로 처리 할 필요가 있나? 이미 0 아닌가
                    Q.append((x, y))
                    cnt+=1
            res.append(cnt)

print(len(res))
res.sort()
for x in res:
    print(x)