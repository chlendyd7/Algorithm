dx=[1,0,-1,0]
dy=[0,1,0,-1]

def DFS(x,y,h):
    ch[xx][y]=1
    for k in range(4):
        xx=x+dx[k]
        yy=y+dy[k]
        if 0<=xx<n and 0<=yy<n and board[xx][yy]>h and ch[xx][yy]==0:
            DFS(xx,yy,h)

n=int(input())
board=[list(map(int,input().split()))for _ in range(n)]
res = 10000000
for h in range(100):
    cnt=0
    ch=[[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if ch[i][j]==0 and board[i][j]>h:
                cnt+=1
                DFS(i,j,h)
    DFS(i)
    if cnt==0:
        break