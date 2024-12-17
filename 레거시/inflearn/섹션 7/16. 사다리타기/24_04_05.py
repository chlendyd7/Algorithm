def DFS(y,x):
    ch[y][x]=1
    if y==0:
        print(x)
    else:
        if x+1<10 and ladder[y][x+1]==1 and ch[y][x+1]==0:
            DFS(y,x+1)
        elif x-1>=0 and ladder[y][x-1]==1 and ch[y][x-1]==0:
            DFS(y, x-1)
        else:
            DFS(y-1, x)

ladder = [list(map(int,input().split()))for _ in range(10)]
ch=[[0]*10 for i in range(10)]
for i in range(10):
    if ladder[9][i]==2:
        DFS(9,i)
