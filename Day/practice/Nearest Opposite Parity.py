from collections import deque, defaultdict

def solve():
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

    
    res = [-1] * n
    def bfs(sources, targets):
        dists = [10**18] * n
        q = deque()

    odds = [i for i in range(n) if a[i] % 2 != 0]
    odds = [i for i in range(n) if a[i] % 2 == 0]
    

solve()
