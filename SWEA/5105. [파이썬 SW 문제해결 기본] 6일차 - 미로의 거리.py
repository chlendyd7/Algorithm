from collections import deque

DIRECTION = [
    (1,0),
    (-1,0),
    (0,1),
    (0,-1)
]
def solution():
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                start = (i, j)
    q = deque([start])
    visited = [[0] * N for _ in range(N)]

    cnt = -1
    while q:
        for _ in range(len(q)):
            r, c = q.popleft()
            if maze[r][c] == 3:
                return cnt

            for dr, dc in DIRECTION:
                nr, nc = r + dr, c + dc
                if 0 <= nr < N and 0 <= nc < N:
                    if maze[nr][nc] != 1 and not visited[nr][nc]:
                        visited[nr][nc] = 1
                        q.append((nr, nc))

        cnt += 1
    return 0


T = int(input())
for t in range(1, T+1):
    print(f'#{t} {solution()}')