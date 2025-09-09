from collections import deque
import sys
sys.stdin = open('A1_input.txt', 'r')
# 방향: 상, 우, 하, 좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(start_x, start_y, start_dir, target, N, grid):
    """
    BFS로 start -> target까지 최소 회전 횟수를 구한다.
    """
    visited = [[[float('inf')] * 4 for _ in range(N)] for _ in range(N)]
    q = deque()
    q.append((start_x, start_y, start_dir, 0))  # (x, y, 방향, 회전횟수)
    visited[start_x][start_y][start_dir] = 0

    while q:
        x, y, direction, rotate_count = q.popleft()

        # 목표 지점 도착 시 회전 횟수 반환
        if (x, y) == target:
            return rotate_count, direction

        # 1) 현재 방향으로 전진
        nx, ny = x + dx[direction], y + dy[direction]
        if 0 <= nx < N and 0 <= ny < N:
            if visited[nx][ny][direction] > rotate_count:
                visited[nx][ny][direction] = rotate_count
                q.append((nx, ny, direction, rotate_count))

        # 2) 오른쪽으로 회전 (제자리에서 단 한 번만)
        nd = (direction + 1) % 4
        if visited[x][y][nd] > rotate_count + 1:
            visited[x][y][nd] = rotate_count + 1
            q.append((x, y, nd, rotate_count + 1))

    return float('inf'), start_dir  # 도달 불가


def solve():
    T = int(input().strip())
    for tc in range(1, T + 1):
        N = int(input().strip())
        grid = [list(map(int, input().split())) for _ in range(N)]

        # 사과 위치 추출 (1번 ~ M번 순서대로)
        apples = []
        for i in range(N):
            for j in range(N):
                if grid[i][j] > 0:
                    apples.append((grid[i][j], i, j))
        apples.sort()  # 사과 번호순으로 정렬

        # 시작점
        x, y, direction = 0, 0, 1  # 시작 방향은 오른쪽(1)
        total_rotate = 0

        # 사과를 순서대로 먹기
        for _, tx, ty in apples:
            rotate_used, new_dir = bfs(x, y, direction, (tx, ty), N, grid)
            total_rotate += rotate_used
            x, y, direction = tx, ty, new_dir  # 위치 및 방향 갱신

        print(f"#{tc} {total_rotate}")


if __name__ == "__main__":
    solve()