def DFS(L, s):
    global res
    if L==m:
        cnt=0
        for i in range(len(house)):
            house_x,house_y=house[i]
            dis=100000
            for j in range(m):
                ch_x, ch_y = ch[j]
                dis=min(dis,abs(abs(house_x-ch_x)+abs(house_y-ch_y)))
            cnt+=dis
        res=min(res, cnt)
    else:
        for i in range(s,len(pizza)):
            ch[L]=pizza[i]
            DFS(L+1,i+1)

n,m=map(int,input().split())
board=[list(map(int,input().split())) for _ in range(n)]
pizza=[]
house=[]
for i in range(n):
    for j in range(n):
        if board[i][j]==1:
            house.append((i,j))
        elif board[i][j]==2:
            pizza.append((i,j))
ch=[0]*m
res=10e9
DFS(0,0)
print(res)