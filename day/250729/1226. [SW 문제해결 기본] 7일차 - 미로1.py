from collections import deque


direction = [
    (1,0),
    (0,1),
    (-1,0),
    (0,-1)
]

def solution():
    N = input()
    board = [list(map(int, input())) for _ in range(16)]
    visited = [[0] * 16 for _ in range(16)]
    q = deque()
    q.append([1, 1])
    visited[1][1] = True
    while q:
        x, y = q.popleft()
        if board[x][y] == 3:
            return 1
        
        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if (0 <= nx < 16 and 0<= ny < 16):
                if not visited[nx][ny] and board[nx][ny] != 1:
                    visited[nx][ny] = True
                    q.append([nx, ny])

    return 0


for t in range(1, 11):
    print(f'#{t} {solution()}')