def DFS(L, sum):
    global res
    if L==n+1: # 상담을 하는 날 다음
        if sum>res:
            res=sum
    else:
        if L+T[L]<=n+1:
            DFS(L+T[L], sum+P[L])
        DFS(L+1, sum)




if __name__=="__main__":
    n= int(input())
    T=list()
    P=list()
    for i in range(n):
        a,b = map(int,input().split())
        T.append(a)
        P.append(b)
    res = -214700000
    T.insert(0,0)
    P.insert(0,0)
    DFS(1,0)
    print(res)