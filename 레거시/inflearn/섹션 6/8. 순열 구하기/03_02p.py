def DFS(L):
    global cnt
    if L==m:
        for j in range(m):
            print(res[j], end=' ')
        print()
        cnt+=1
    else:
        for i in range(1,n+1):
            if ch[i] == 0:
                ch[i] = 1
                res[L] = i
                DFS(L+1)
                ch[i] = 0




if __name__=="__main__":
    n,m = map(int,input().split())
    ch =[0]*(n+1)
    res = [0]*m
    cnt = 0
    DFS(0)