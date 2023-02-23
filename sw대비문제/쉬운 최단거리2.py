
import collections
import sys


input = sys.stdin.readline

dt=[(-1,0),(1,0),(0,-1),(0,1)]

n,m= map(int,input().split())
board = [list(map(int,input().split())) for _ in range(m)]

def find_start():
    for i in range(n):
        for j in range(m):
            if board[i][j] == 2:
                return i,j

start_i, start_j = find_start()

vboard = [[-1]*m for _ in range(n)]
q = collections.deque()
q.append((start_i,start_j))
vboard[start_i][start_j]=0

while q:
    i, j = q.popleft()

    for k in range(4):
        ni, nj = i + dt[k][0], j + dt[k][1]
        if 0<= ni < n and 0<= nj < m and vboard[ni][nj]==-1:
            if board[ni][nj] == 1:
                vboard[ni][nj] = vboard[i][j] +1
                q.append((ni,nj))
            elif board[ni][nj] == 0:
                    vboard[ni][nj] = 0

for i in range(n):
    for j in range(m):
        if board[i][j] == 0:
            print(0, end=' ')
        else:
            print(vboard[i][j], end=' ')
    print()