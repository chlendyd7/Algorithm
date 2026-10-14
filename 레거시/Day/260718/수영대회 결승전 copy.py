from collections import deque

def solution():
    n = int(input())
    maze = [list(map(int, input().split())) for _ in range(n)]
    sx, sy = map(int, input().split())
    ex, ey = map(int, input().split())

    q = deque()
    q.append((sx, sy, 0))

    visited = [[-1] * n for _ in range(n)]
    visited[sx][sy] = 0

    directions = [(0,1), (1,0), (-1,0), (0,-1)]

    while q:
        x, y, time = q.popleft()

        if (x, y) == (ex, ey):
            return time

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if not (0 <= nx < n and 0 <= ny < n):
                continue
            if maze[nx][ny] == 1:
                continue

            # 일반 칸
            if maze[nx][ny] == 0:
                if visited[nx][ny] == -1 or visited[nx][ny] > time + 1:
                    visited[nx][ny] = time + 1
                    q.append((nx, ny, time + 1))

            # 소용돌이 칸
            elif maze[nx][ny] == 2:
                # 소용돌이는 time % 3 == 2 일 때만 진입 가능
                if time % 3 == 2:
                    if visited[nx][ny] == -1 or visited[nx][ny] > time + 1:
                        visited[nx][ny] = time + 1
                        q.append((nx, ny, time + 1))
                else:
                    # 아직 못 들어가면 현재 자리에서 기다리기
                    if visited[x][y] < time + 1:
                        visited[x][y] = time + 1
                        q.append((x, y, time + 1))

    return -1


T = int(input())
for tc in range(1, T + 1):
    print(f"#{tc} {solution()}")
