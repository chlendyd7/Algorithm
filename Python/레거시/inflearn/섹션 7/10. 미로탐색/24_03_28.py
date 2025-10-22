


def DFS(x, y):
    global cnt
    if x==6 and y==6:
        cnt +=1
    else:
        for i in range(4):
            xx=x+dx[i]
            yy=y+dy[i]
            if 0<=xx<7 and 0<=yy<7 and board[xx][yy] == 0:
                board[xx][yy]=1
                DFS(xx,yy)
                board[xx][yy]=0


cnt=0
dx=[-1, 0, 1, 0]
dy=[0, 1, 0, -1]
board=[list(map(int, input().split())) for _ in range(7)]
board[0][0]=1
DFS(0,0)
print(cnt)