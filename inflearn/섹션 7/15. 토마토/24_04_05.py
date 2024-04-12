from collections import deque
import sys
sys.stdin=open("/Users/doyoungchoi/Documents/GitHub/Algorithm/inflearn/파이썬 알고리즘 문제풀이(코딩테스트 대비)/섹션 7/15. 토마토/in1.txt", "r")
dx=[-1,0,1,0]
dy=[0,-1,0,1]
m,n = map(int,input().split())
board = [list(map(int,input().split()))for _ in range(n)]
Q=deque()
for i in range(n):
    for j in range(m):
        if board[i][j]==1:
            Q.append((i,j))
            
while Q:
    x,y = Q.popleft()
    for k in range(4):
        xx=x+dx[k]
        yy=y+dy[k]
        if 0<=xx<n and 0<=yy<m and board[xx][yy]==0 and not board[xx][yy]==-1:
            board[xx][yy]=board[x][y]+1
            Q.append((xx,yy))

for i in range(n):
    for j in range(m):
        if board[i][j]==0:
            print('-1')
            exit()
print(max(max(b)for b in board)-1)

