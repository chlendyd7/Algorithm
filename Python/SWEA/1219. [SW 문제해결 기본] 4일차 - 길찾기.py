from collections import defaultdict, deque

def solution():
    _, N = map(int, input().split())
    visited = [0] * 100
    board = list(map(int, input().split()))

    graph = defaultdict(list)
    for i in range(0, N*2, 2):
        graph[board[i]].append(board[i+1])

    q = deque()
    q.append(0)
    while q:
        now = q.popleft()
        if now == 99:
            return 1
        for next in graph[now]:
            if not visited[next]:
                visited[next] = 1
                q.append(next)
    
    return 0

# T = int(input())
for t in range(1, 11):
    print(f'#{t} {solution()}')

