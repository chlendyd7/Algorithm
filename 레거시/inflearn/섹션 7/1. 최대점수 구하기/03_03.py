def DFS(L, sum, time):
    global cnt
    if time > m:
        return
    if L > n:
        return
    if L == n:
        if sum>cnt:
            cnt = sum
    else:
        DFS(L+1, sum+pv[L], time+pt[L])
        DFS(L+1, sum, time)



if __name__=="__main__":
    n,m = map(int,input().split())
    pv = list()
    pt = list()
    for i in range(n):
        a, b = map(int, input().split())
        pv.append(a)
        pt.append(b)
    cnt = 0
    DFS(0,0,0)
    print(cnt)
        