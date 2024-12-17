n,m = map(int,input().split())
ls = [[0]*(n+1) for _ in range(n+1)]
for i in range(m):
    a,b,c = map(int, input().split())
    ls[a][b] = c

for i in range(1, n+1):
    for j in range(1, n+1):
        print(ls[i][j], end=' ')
    print()
