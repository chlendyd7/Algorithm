dx=[-1, 0, 1, 0]
dy=[0, 1, 0, -1]


def DFS(x,y):
    global cnt
    cnt+=1
    board[x][y]=0
    for i in range(4):
        xx=x+dx[i]
        yy=y+dy[i]
        if 0<=xx<n and 0<=yy<n and board[xx][yy]==1:
            board[xx][yy]=0
            DFS(xx,yy)
    




if __name__=='__main__':
    n=int(input())
    check_lis=[]
    board=[list(map(int,input())) for _ in range(n)]
    res=[]
    for i in range(n):
        for j in range(n):
            if board[i][j]==1:
                cnt=0
                DFS(i,j)
                res.append(cnt)
    print(len(res))
    res.sort()
    for x in res:
        print(x)
            