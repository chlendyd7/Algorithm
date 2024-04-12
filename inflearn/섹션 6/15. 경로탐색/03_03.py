def DFS(v):
    global cnt
    if v==n:
        cnt+=1
        for x in path:
            print(x, end=' ')
        print()
    else:
        for i in range(1, n+1):
            if g[v][i] == 1 and ch[i]==0: #현재노드에서 가려는 곳으로 갈 수 있는가 [v][i]
                ch[i] = 1
                path.append(i)
                DFS(i)
                path.pop() # 넣었던거 뺴야함
                ch[i]=0




if __name__=="__main__":
    n,m = map(int,input().split())
    g = [[0]*(n+1) for _ in range(n+1)]
    ch=[0]*(n+1)
    for i in range(m):
        a,b = map(int,input().split())
        g[a][b] = 1
    cnt = 0
    path = [] #경로 저장
    path.append(1)
    ch[1] = 1 # 1번노드 방문 했다
    DFS(1)
    print(cnt)