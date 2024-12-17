def DFS(L,v):
    global cnt
    if L==m:
        for j in range(m):
            print(res[j], end=' ')
        print()
        cnt+=1
    else:
        for i in range(v,n+1):
            res[L]=i
            DFS(L+1, i+1)
    





if __name__ == "__main__":
    n,m = map(int,input().split())
    cnt = 0
    res = [0]*m
    DFS(0,1)
    print(cnt)
