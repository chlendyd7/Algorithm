from collections import deque


direction = [
    (-1, 0),
    (1, 0),
    (0, 1),
    (0, -1)
]

M, N = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]

q = deque()
zero_count = 0
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            visited[i][j] = 1
            q.append((i,j))
        elif graph[i][j] == 0:
            zero_count += 1

days = -1
while q:
    size_q = len(q)
    days += 1
    for _ in range(size_q):
        r, c = q.popleft()

        for dx, dy in direction:
            nr = r + dx
            nc = c + dy

            if 0 <= nr < N and 0 <= nc < M:
                if graph[nr][nc] == 0 and not visited[nr][nc]:
                    visited[nr][nc] = 1
                    q.append((nr, nc))
                    zero_count -= 1

if zero_count == 0:
    print(days)
else:
    print(-1)
