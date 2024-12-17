

def DFS(L,s):
    global res
    if L==m:
        sum=0
        for i in range(len(hs)):
            x1=hs[i][1]
            y1=hs[i][0]
            dis=1000000
            for k in cn:
                x2=pz[k][1]
                y2=pz[k][0]
                dis=min(dis, abs(x1-x2)+abs(y1-y2))
            sum+=dis
        if res>sum:
            res=sum
    else:
        for i in range(s, len(pz)):
            cn[L]=i
            DFS(L+1,i+1)





if __name__=="__main__":
    n,m=map(int, input().split())
    board=[list(map(int,input().split())) for _ in range(n)]
    hs=[]
    pz=[]
    res=1000000
    cn=[0]*m
    for i in range(n):
        for j in range(n):
            if board[i][j]==1:
                hs.append((i,j))
            elif board[i][j]==2:
                pz.append((i,j))

    DFS(0,0)
    print(res)