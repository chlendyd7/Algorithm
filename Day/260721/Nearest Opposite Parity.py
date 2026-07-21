from collections import deque, defaultdict
INF = 10**18
def solve():
    def bfs(sources, targets):
        dist = [10**18] * n
        q = deque()
        
        for s in sources:
            dist[s] = 0
            q.append(s)
        
        while q:
            u = q.popleft()
            
            for v in rev_adj[u]:
                if dist[v] == 10**18:
                    dist[v] = dist[u] + 1
                    q.append(v)

            for t in targets:
                if dist[t] != INF:
                    res[t] = dist[t]

    n = int(input())
    a = list(map(int, input().split()))
    
    rev_adj = defaultdict(list)
    for i in range(n):
        left = i - a[i]
        right = i + a[i]
        if left >= 0:
            rev_adj[left].append(i)
        if right < n:
            rev_adj[right].append(i)
    
    odds = [i for i in range(n) if a[i] %2 !=0]
    evens = [i for i in range(n) if a[i] %2 ==0]
    res = [-1] * n

    bfs(odds, evens)
    bfs(evens, odds)
    
    

    print(' '.join(map(str, res)))
solve()
