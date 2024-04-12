def DFS(L,s):
    global res
    if L==m:
        sum=0
        for j in range(len(hs)):
            x1=hs[j][0]
            y1=hs[j][1]
            dis=21470000
            for x in cb: # 피자 집 계속 바뀐 것 중에 최소 값
                x2=pz[x][0]
                y2=pz[x][1]
                dis=min(dis, abs(x1-x2) + abs(y1-y2))
            sum+=dis # 각 도시의 총 합
        if sum<res:
            res=sum
        for x in cb:
            print(x, end='')
        print()
    else:
        for i in range(s, len(pz)):
            cb[L]=i
            DFS(L+1, i+1)




if __name__=="__main__":
    n,m = map(int,input().split())
    board = [list(map(int,input().split())) for _ in range(n)]
    hs = []
    pz = []
    cb = [0]*m # 살아남는 갯수
    res = 21470000
    for i in range(n):
        for j in range(n):
            if board[i][j]==1:
                hs.append((i,j))
            elif board[i][j]==2:
                pz.append((i,j))
    DFS(0,0)