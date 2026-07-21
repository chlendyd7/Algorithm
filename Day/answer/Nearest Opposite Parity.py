from collections import deque, defaultdict

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    # 역방향 그래프 구성
    rev_adj = defaultdict(list)
    
    for i in range(n):
        left = i - a[i]
        right = i + a[i]
        if left >= 0:
            rev_adj[left].append(i)
        if right < n:
            rev_adj[right].append(i)
    
    res = [-1] * n
    
    # 다중 소스 BFS 함수
    def bfs(sources, targets):
        dists = [float('inf')] * n
        q = deque()
        
        # 모든 시작점을 큐에 넣기
        for s in sources:
            dists[s] = 0
            q.append(s)
        
        # BFS 수행
        while q:
            u = q.popleft()
            
            for v in rev_adj[u]:
                if dists[v] == float('inf'):
                    dists[v] = dists[u] + 1
                    q.append(v)
        
        # 타겟 정점들의 거리만 기록
        for t in targets:
            if dists[t] != float('inf'):
                res[t] = dists[t]
    
    # 홀수/짝수 위치 분류
    odds = [i for i in range(n) if a[i] % 2 != 0]
    evens = [i for i in range(n) if a[i] % 2 == 0]
    
    # BFS 1: 모든 홀수 위치 → 짝수 위치까지 거리
    bfs(odds, evens)
    
    # BFS 2: 모든 짝수 위치 → 홀수 위치까지 거리
    bfs(evens, odds)
    
    # 결과 출력
    print(' '.join(map(str, res)))

solve()
