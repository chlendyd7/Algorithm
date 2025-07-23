'''
    - 같은 정점의 번호가 등장 할 수 없다 => visited[] 체크
    - 두 정점을 연결하는 간선이 존재해야한다
'''
from collections import defaultdict
def solution():
    N, M = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(M):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    max_length = 0

    def dfs(node, visited, length):
        nonlocal max_length
        max_length = max(length, max_length)
        
        for n in graph[node]:
            if not visited[n]:
                visited[n] = True
                dfs(n, visited, length + 1)
                visited[n] = False

    for start in range(1, N+1):
        visited = [False] * (N+1)
        visited[start] = True
        dfs(start, visited, 1)

    return max_length

T = int(input())
for t in range(1, T+1):
    print(f'#{t} {solution()}')
