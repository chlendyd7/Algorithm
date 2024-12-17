from collections import deque
import sys
sys.stdin=open("inflearn\파이썬 알고리즘 문제풀이(코딩테스트 대비)\섹션 7\\15. 토마토\in4.txt", "r")
dx = [-1,0,1,0]
dy = [0,1,0,-1]

n,m = map(int,input().split())
board=[list(map(int,input().split()))for _ in range(m)]
Q=deque()

for i in range(m):
    for j in range(n):
        if board[i][j]==1:
            Q.append((i,j))
while Q:
    x,y=Q.popleft()
    for i in range(4):
        xx=x+dx[i]
        yy=y+dy[i]
        if 0<=xx<m and 0<=yy<n and board[xx][yy]==0:
            board[xx][yy]=board[x][y]+1
            Q.append((xx,yy))

result=0
for i in range(m):
    for j in range(n):
        if board[i][j]==0:
            print(-1)
            exit()
        elif board[i][j]>result:
            result=board[i][j]
print(result-1)
