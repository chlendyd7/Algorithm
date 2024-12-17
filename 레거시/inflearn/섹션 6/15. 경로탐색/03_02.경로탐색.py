n,m = map(int,input().split())
ls = [[0]*(n+1) for _ in range(n)]
for i in range(m):
    a,b = map(int,input().split())
    ls[a][b] = 1

