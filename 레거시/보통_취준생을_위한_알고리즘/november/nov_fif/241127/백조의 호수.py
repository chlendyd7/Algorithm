import sys
from collections import deque

input = sys.stdin.readline

# 방향 벡터 (상, 하, 좌, 우)
DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def melt_ice():
    """현재 물과 인접한 얼음을 녹임."""
    while water_queue:
        y, x = water_queue.popleft()
        lake[y][x] = '.'  # 물로 변경

        for dy, dx in DIRECTIONS:
            ny, nx = y + dy, x + dx
            if 0 <= ny < rows and 0 <= nx < cols and not water_visited[ny][nx]:
                if lake[ny][nx] == 'X':  # 인접 얼음은 다음 날 녹을 예정
                    next_water_queue.append((ny, nx))
                water_visited[ny][nx] = True


def can_swans_meet():
    """백조가 서로 만날 수 있는지 확인."""
    while swan_queue:
        y, x = swan_queue.popleft()

        if (y, x) == swan_end:
            return True

        for dy, dx in DIRECTIONS:
            ny, nx = y + dy, x + dx
            if 0 <= ny < rows and 0 <= nx < cols and not swan_visited[ny][nx]:
                if lake[ny][nx] == '.':  # 물이면 즉시 이동 가능
                    swan_queue.append((ny, nx))
                elif lake[ny][nx] == 'X':  # 얼음은 다음 날 이동 가능
                    next_swan_queue.append((ny, nx))
                swan_visited[ny][nx] = True

    return False


if __name__ == "__main__":
    rows, cols = map(int, input().split())
    lake = [list(input().strip()) for _ in range(rows)]

    # 방문 체크 배열
    swan_visited = [[False] * cols for _ in range(rows)]
    water_visited = [[False] * cols for _ in range(rows)]

    # BFS 큐 초기화
    swan_queue = deque()
    next_swan_queue = deque()
    water_queue = deque()
    next_water_queue = deque()

    # 백조와 물 위치 초기화
    swan_start = None
    swan_end = None

    for i in range(rows):
        for j in range(cols):
            if lake[i][j] == 'L':
                if not swan_start:
                    swan_start = (i, j)
                    swan_queue.append(swan_start)
                    swan_visited[i][j] = True
                else:
                    swan_end = (i, j)
                lake[i][j] = '.'  # 백조가 있는 칸은 물로 취급
                water_queue.append((i, j))
                water_visited[i][j] = True
            elif lake[i][j] == '.':
                water_queue.append((i, j))
                water_visited[i][j] = True

    # BFS로 매일 진행
    days = 0
    while True:
        melt_ice()
        if can_swans_meet():
            print(days)
            break

        # 다음 날을 위한 큐 갱신
        swan_queue = next_swan_queue
        water_queue = next_water_queue
        next_swan_queue = deque()
        next_water_queue = deque()

        days += 1
