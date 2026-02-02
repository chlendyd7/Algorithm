n = int(input())
m = int(input())
inf = float('inf')

dist = [[inf] * (n+1) for _ in range(n+1)]
nxt = [[0] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    dist[i][i] = 0

for i in range(m):
    u,v,w = map(int, input().split())
    if w < dist[u][v]:
        dist[u][v] = w
        nxt[u][v] = v

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]
                nxt[i][j] = nxt[i][k]

for i in range(1, n+1):
    for j in range(1, n+1):
        print(dist[i][j] if dist[i][j] != inf else 0 ,end=" ")
    print()

result = []
for i in range(1, n+1):
    for j in range(1, n+1):
        path = []
        if i==j or dist[i][j] == inf: 
            print(0)
        else:
            curr = i
            while curr != j:
                path.append(curr)
                curr = nxt[curr][j]
            path.append(j)
            print(len(path), *path)
