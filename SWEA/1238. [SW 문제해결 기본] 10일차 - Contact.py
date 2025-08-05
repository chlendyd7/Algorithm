from collections import defaultdict, deque


def solution():
    N, start = map(int, input().split())
    graph = defaultdict(list)
    board = list(map(int, input().split()))
    for i in range(0, N, 2):
        from_, to = board[i], board[i+1]
        graph[from_].append(to)

    visited = [0] * 101
    depth_graph = defaultdict(list)

    q = deque([(start, 0)])
    visited[start] = 1
    while q:
        now, depth = q.popleft()
        depth_graph[depth].append(now)

        for next in graph[now]:
            if not visited[next]:
                visited[next] = 1
                q.append((next, depth+1))

    max_depth = max(depth_graph.keys())
    return max(depth_graph[max_depth])


for t in range(1, 11):
    print(f'#{t} {solution()}')
