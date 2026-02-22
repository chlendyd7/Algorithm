

def DFS(L, sum):
    if L==n and sum==f:
        for x in p:
            
    else:
        for i in range(1,n+1):
            if ch[i]==0:
                ch[i]=1
                p[L] = i
                DFS(L+1, sum+)
            DFS(L+1, sum+i)




if __name__ == "__main__":
    n,f = map(int,input().split())
    p=[0]*n
    b = [1]*n+1
    ch = [0]*(n+1)
    DFS(0,0)