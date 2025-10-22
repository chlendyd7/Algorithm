from collections import defaultdict, deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def solution():
    N, M, K = map(int, input().split())
    initial = [list(map(int, input().split())) for _ in range(N)]

    size = N + 2 * K
    offset = K
    grid = [[0] * size for _ in range(size)]

    cells = deque()
    for i in range(N):
        for j in range(M):
            if initial[i][j] > 0:
                x, y, = i + offset, j + offset
                life = initial[i][j]
                grid[x][y] = life
                cells.append([x,y,life, 0, life])

    for _ in range(K):
        new_cells = defaultdict(list)
        q_len = len(cells)
        for _ in range(q_len):
            x, y, life, status, time_life = cells.popleft()
            if status == 0:
                time_life -= 1
                if time_life == 0:
                    status = 1
                    time_life = life
                cells.append([x,y,life,status, time_life])
            elif status == 1:
                for d in range(4):
                    nx, ny = x + dx[d], y + dy[d]
                    if grid[nx][ny] == 0:
                        new_cells[(nx, ny)].append(life)
                time_life -= 1
                if time_life > 0:
                    cells.append([x,y,life,status, time_life])
                else:
                    grid[x][y] = -1

    for (nx, ny), lifes in new_cells.items():
        max_life = max(lifes)
        if grid[nx][ny] == 0:
            grid[nx][ny] = max_life
            cells.append([nx, ny, max_life, 0, max_life])

T = int(input())
for t in range(1, T+1):
    print(f'#{t} {solution()}')
