from collections import deque
import sys
input = sys.stdin.readline

direction = [
    (1,0),
    (-1,0),
    (0,1),
    (0,-1)
]

N, M, K = map(int, input().split())
board = [list(map(int, input().strip())) for _ in range(N)]
visited = [[1e9] * M for _ in range(N)]
visited[0][0] = 0

def solution():
    days = 0
    q = deque([(0,0)])
    while q:
        size_q = len(q)
        days += 1
        for _ in range(size_q):
            r, c = q.popleft()
            wall = visited[r][c]

            if r == N-1 and c == M-1:
                return days

            for dr, dc in direction:
                nr, nc = r + dr, c + dc
                if 0 <= nr < N and 0 <= nc < M:
                    if board[nr][nc] == 0:
                        if wall < visited[nr][nc]:
                            visited[nr][nc] = wall
                            q.append((nr, nc))
                    else: # 벽일 때
                        if wall + 1 <= K and wall + 1 < visited[nr][nc]:
                            visited[nr][nc] = wall + 1
                            q.append((nr, nc))

    return -1

print(solution())
