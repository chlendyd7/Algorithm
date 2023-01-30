#최단거리는 무조건 BFS 
import sys
from collections import deque
sys.stdin=open("input.txt", "r")
dx=[-1, 0, 1, 0]
dy=[0, 1, 0, -1]
board=[list(map(int, input().split())) for _ in range(7)]
dis=[[0]*7 for _ in range(7)]
Q=deque()
Q.append((0, 0))
board[0][0]=1
while Q:
    tmp=Q.popleft() # 현재 좌표
    for i in range(4):
        x=tmp[0]+dx[i]
        y=tmp[1]+dy[i]
        if 0<=x<=6 and 0<=y<=6 and board[x][y]==0: # 경계선 밖으로 나가지 않게
            board[x][y]=1
            dis[x][y]=dis[tmp[0]][tmp[1]]+1
            Q.append((x, y))
if dis[6][6]==0: # 벽에 막혀 도착 못함
    print(-1)
else:
    print(dis[6][6])