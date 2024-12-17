
def DFS(L, sum):
    global res
    if L==n+1:
        if sum>res:
            res=sum
    else:
        if L+T[L]<=n+1:
            DFS(L+T[L], sum+P[L])# 상담을 한 날짜
        DFS(L+1, sum)# 상담을 하지 않았을 때




if __name__=="__main__":
    n=int(input()) #7 날짜
    T=list()
    P=list()
    for i in range(n):
        a, b=map(int, input().split())
        T.append(a)
        P.append(b)
    res=-2147000000
    T.insert(0, 0)
    P.insert(0, 0)
    DFS(1, 0)
    print(res)