def DFS(L, sum):
    global res
    if L==n+1:
        if sum>res:
            res=sum
    else:
        if L+pv[L]<=n+1:
            DFS(L+pv[L], sum+pt[L])
        DFS(L+1, sum)



if __name__=='__main__':
    n=int(input())
    pv = list()
    pt = list()
    for i in range(n):
        a, b = map(int,input().split())
        pv.append(a)
        pt.append(b)
    res=0
    DFS(1,0)
    print(res)