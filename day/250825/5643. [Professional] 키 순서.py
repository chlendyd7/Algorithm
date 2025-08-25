from collections import defaultdict, deque
def bfs(start, N, graph):
    visited = [0] * (N+1)
    q = deque([start])
    cnt = 1
    visited[start] = 1
    while q:
        now = q.popleft()
        for next in graph[now]:
            if not visited[next]:
                visited[next] = 1
                q.append(next)
                cnt += 1

    return cnt

def solution():
    N = int(input())
    M = int(input())
    bigger = defaultdict(list)
    smaller = defaultdict(list)
    for _ in range(M):
        a, b = map(int, input().split())
        bigger[a].append(b)
        smaller[b].append(a)
    
    result = 0
    for i in range(1, N+1):
        big = bfs(i, N, bigger)
        small = bfs(i, N, smaller)
        if big + small == N-1:
            result += 1
    return result


T = int(input())
for t in range(1, T+1):
    print(f'#{t} {solution()}')