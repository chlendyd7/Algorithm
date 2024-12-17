def DFS(L, sum):
    global res
    if L==n:
        if 0<sum<=s:
            res.add(sum) 
    
    else:
        DFS(L+1, sum+G[L]) # 추를 왼쪽에 넣는다 
        DFS(L+1, sum-G[L]) # 추를 오른쪽에 놓는다
        DFS(L+1, sum) # index에 추를 사용하지 않는다



if __name__=="__main__":
    n=int(input())
    G=list(map(int,input().split()))
    s=sum(G)
    res=set() # 중복되면 안됨
    DFS(0,0)
    print(s-len(res))