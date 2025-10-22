dx = [-1,0,1,0]
dy = [0,1,0,-1]
n=int(input())
board = [list(map(int,input()))for _ in range(n)]
cnt = 0
res = []
Q= deque()
for i in range(n):
    for j in range(n):
        if board[i][j]==1:
            board[i][j]=0
            Q.append((i,j))