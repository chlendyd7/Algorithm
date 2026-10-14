n,m = map(int, input().split())
edges = []
for _ in range(m):
    s,e,w = map(int, input().split())
    edges.append([s,e,w])

inf = float('inf')
dist = [inf] * (n+1)
dist[1] = 0
check_inf = False
for i in range(n):    
    for s,e,w in edges:
        if dist[s] != inf and dist[e] > dist[s] + w:
            if i == n - 1:
                check_inf = True
            dist[e] = dist[s] + w

if check_inf:
    print(-1)
else:
    for i in range(2, n+1):
        if dist[i] == inf:
            print(-1)
        else:
            print(dist[i])
