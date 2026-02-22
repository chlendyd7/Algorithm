dx=[-1, 0, 1, 0]
dy=[0, 1, 0, -1]

def DFS(x, y):
    global cnt
    if x==mx and y==my:
        cnt+=1
    else:
        for i in range(4):
            xx=x+dx[i]
            yy=y+dy[i]
            if 0<=xx<n and 0<=yy<n and board[xx][yy]>board[x][y] and ch[xx][yy]==0:
                ch[xx][yy]=1
                DFS(xx,yy)
                ch[xx][yy]=0





if __name__=='__main__':
    n=int(input())
    board=[[0]*n for _ in range(n)]
    ch=[[0]*n for _ in range(n)]
    max=-214700000
    min=214700000
    cnt=0
    for i in range(n):
        tmp=list(map(int,input().split()))
        for j in range(n):
            if tmp[j]<min:
                sx=i
                sy=j
                min=tmp[j]
            if tmp[j]>max:
                mx=i
                my=j
                max=tmp[j]
            board[i][j] = tmp[j]
    ch[sx][sy]=1
    DFS(sx,sy)
    print(cnt)