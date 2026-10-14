# https://www.acmicpc.net/problem/11657
INF = float('inf')

n, m = map(int, input().split())
edges = []
for _ in range(m):
    edges.append(list(map(int, input().split())))

def bellman_ford(start, n, edges):
    dist = [INF] * (n+1)
    dist[start] = 0
    negative_cycle = False

    for i in range(n):
        for u, v, w in edges:
            if dist[u] != INF and dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                if i == n -1 :
                    negative_cycle = True

    if negative_cycle:
        print(-1)
    else:
        for i in range(2, n+1):
            if dist[i] == INF:
                print(-1)
            else:
                print(dist[i])

bellman_ford(1, n, edges)
