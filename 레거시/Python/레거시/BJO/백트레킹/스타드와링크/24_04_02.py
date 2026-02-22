


def DFS(L, idx):
    global res
    if L==n//2:
        A=0
        B=0
        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j]==0:
                    B+=board[i][j]
                elif not visited[i] and not visited[j]:
                    A+=board[i][j]
        res=min(res, abs(A-B))
        return
        visited



n=int(input())
board=[list(map(int,input().split())) for _ in range(n)]
visited = [[0]for _ in range(n)]
res = 2147000000
DFS(0,0)
print(res)