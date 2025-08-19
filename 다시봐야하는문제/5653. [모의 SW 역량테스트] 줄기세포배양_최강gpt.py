from collections import deque, defaultdict
from time import time
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

T = int(input())
for test_case in range(1, T+1):
    n, m, k = map(int, input().split())
    initial = [list(map(int, input().split())) for _ in range(n)]

    # 충분히 큰 공간 확보
    size = n + 2*k
    offset = k
    grid = [[0]*size for _ in range(size)]

    # 세포 큐: x, y, life, 상태(0=비활성,1=활성), 남은 시간
    cells = deque()
    for i in range(n):
        for j in range(m):
            if initial[i][j] > 0:
                x, y = i+offset, j+offset
                life = initial[i][j]
                grid[x][y] = life
                cells.append([x, y, life, 0, life])

    for _ in range(k):
        new_cells = defaultdict(list)
        q_len = len(cells)
        for _ in range(q_len):
            x, y, life, status, time_left = cells.popleft()

            if status == 0:  # 비활성
                time_left -= 1
                if time_left == 0:
                    status = 1
                    time_left = life
                cells.append([x, y, life, status, time_left])
            elif status == 1:  # 활성
                # 번식
                for d in range(4):
                    nx, ny = x+dx[d], y+dy[d]
                    if grid[nx][ny] == 0:
                        new_cells[(nx, ny)].append(life)
                # 활성시간 감소
                time_left -= 1
                if time_left > 0:
                    cells.append([x, y, life, status, time_left])
                else:
                    grid[x][y] = -1

        # 새로 번식한 세포 처리
        for (nx, ny), lifes in new_cells.items():
            max_life = max(lifes)
            if grid[nx][ny] == 0:
                grid[nx][ny] = max_life
                cells.append([nx, ny, max_life, 0, max_life])

    print(f"#{test_case} {len(cells)}")
