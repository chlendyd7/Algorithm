from collections import deque

def solution(maps):
    rows, cols = len(maps), len(maps[0])
    
    # 시작점, 레버, 출구 위치 찾기
    start, lever, exit = None, None, None
    for r in range(rows):
        for c in range(cols):
            if maps[r][c] == 'S':
                start = (r, c)
            elif maps[r][c] == 'L':
                lever = (r, c)
            elif maps[r][c] == 'E':
                exit = (r, c)

    # BFS로 최단 거리 탐색
    def bfs(start, target):
        queue = deque([(start[0], start[1], 0)])  # (row, col, distance)
        visited = [[False] * cols for _ in range(rows)]
        visited[start[0]][start[1]] = True

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상하좌우

        while queue:
            x, y, dist = queue.popleft()
            if (x, y) == target:
                return dist
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols and not visited[nx][ny] and maps[nx][ny] != 'X':
                    visited[nx][ny] = True
                    queue.append((nx, ny, dist + 1))
        
        return -1

    # 경로 계산
    to_lever = bfs(start, lever)
    if to_lever == -1:  # 레버에 도달 불가
        return -1

    to_exit = bfs(lever, exit)
    if to_exit == -1:  # 출구에 도달 불가
        return -1

    return to_lever + to_exit
