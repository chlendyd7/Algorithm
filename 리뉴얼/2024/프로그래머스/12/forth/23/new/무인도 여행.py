from collections import deque

def bfs(y, x, i, j, maps, visited):
    direction = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    q = deque()
    q.append([i, j])
    visited[i][j] = True
    cnt = 0
    while q:
        now_y, now_x = q.popleft()
        cnt += int(maps[now_y][now_x])  # 숫자 값을 더해야 하므로 형 변환 추가

        for k in range(4):
            dy = direction[k][0] + now_y
            dx = direction[k][1] + now_x
            if 0 <= dy < y and 0 <= dx < x and not visited[dy][dx] and maps[dy][dx] != 'X':
                q.append([dy, dx])
                visited[dy][dx] = True

    return cnt


def solution(maps):
    y, x = len(maps), len(maps[0])
    visited = [[False] * x for _ in range(y)]
    answer = []
    for i in range(y):
        for j in range(x):
            if maps[i][j] != 'X' and not visited[i][j]:
                answer.append(bfs(y, x, i, j, maps, visited))
    if answer:
        return sorted(answer)
    else:
        return [-1]
