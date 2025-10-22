def DFS(v):
    global cnt
    if v==n: # v에 도착하면 cnt+1하게끔
        cnt+=1
        for x in path:
            print(x, end=' ')
        print()
    else:
        for i in range(1, n+1):
            if g[v][i]==1 and ch[i]==0: # 인접 노드로 갈 수 있냐, i에 방문을 하지 않았는가
                ch[i]=1 # 방문했다고 체크
                path.append(i)
                DFS(i)
                path.pop()
                ch[i]=0 # 빽하는 부분 방문한 것을 풀어줘야함




if __name__=="__main__":
    n,m = map(int,input().split())
    g=[[0]*(n+1) for _ in range(n+1)] 
    ch=[0]*(n+1)
    for i in range(m):
        a, b = map(int, input().split())
        g[a][b]=1
    cnt = 0
    path = []
    path.append(1)
    ch[1] = 1
    DFS(1)
    print(cnt)