





def DFS(L, idx):
    global res
    if L==n//2:
        A=0
        B=0
        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j]:
                    A += board[i][j]
                elif not visited[i] and not visited[j]:
                    B += board[i][j]
        res=min(res, abs(A-B))
        return
    for i in range(idx, n):
        visited[i]=True
        DFS(L+1, i+1)
        visited[i]=False
            

n=int(input())
board=[list(map(int,input().split())) for _ in range(n)]
visited = [0] *n
res = 2147000000
DFS(0,0)
print(res)