from collections import defaultdict


def solution():
    graph = defaultdict(list)
    N, M = map(int, input().split())
    max_length = 0
    for _ in range(M):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)

    def dfs(node, visited, depth):
        nonlocal max_length
        max_length = max(max_length, depth)

        for next in graph[node]:
            if not visited[next]:
                visited[next] = True
                dfs(next, visited, depth + 1)
                visited[next] = False

    for start in range(1, N+1):
        visited = [False] * (N+1)
        visited[start] = True
        dfs(start, visited, 1)

    return max_length

T = int(input())
for t in range(1, T+1):
    print(f'#{t} {solution()}')
