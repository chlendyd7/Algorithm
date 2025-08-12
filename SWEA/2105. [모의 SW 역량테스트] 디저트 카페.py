'''
한변의 길이가 N
대각선 방향으로 움직일 수 있음

대각선 방향으로 움직이고 사각형 모양을 그리며 출발한 카페로 돌아와야함
같은 숫자 x

같이 하나의 카페에서 디저트도 안된다

dfs(좌표, 방문여부, 갯수)

'''
direction = [
    (-1,1),
    (1,1),
    (1,-1),
    (-1,-1)
]
def find_max_value(row, col, board):
    mx_count = 0
    N = len(board)
    visited = [[0] * N for _ in range(N)]
    items = [0] * 101
    def dfs(row, col, visited, items):
        nonlocal mx_count
        if row == visited[0][0] and col == visited[0][1]:
            mx_count = max(mx_count, len(items))
            return

        for dx, dy in direction:
            nx, ny = row + dx, col + dy
            if 0 <= nx < N and 0 <= ny < N and not visited and not items[board[nx][ny]]:
                visited[nx][ny] = 1
                items[nx][ny] = 1
                dfs(nx, ny, visited, items)
                visited[nx][ny] = 0
                items[nx][ny] = 0
    
    visited[row][col] = 1
    items[board[row][col]] = 1
    dfs(row, col, visited, items)

    return mx_count

def solution():
    result = 0
    N = int(input())
    board = [list(map(int, input().split()))]
    for i in range(1, N-1):
        for j in range(1, N-1):
            result = max(result, find_max_value(i, j, board))

    return result if result else 0


T = int(input())
for t in range(1, T+1):
    print(f'#{t} {solution()}')
