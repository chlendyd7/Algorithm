from collections import deque


direction = [
    (1,0),
    (0,1),
    (-1,0),
    (0,-1)
]

def solution():
    N = int(input())
    board = [list(map(int, input())) for _ in range(100)]
    q = deque()
    q.append((1,1))
    visited = [[0] * 100 for _ in range(100)]
    visited[1][1] = 1
    while q:
        x, y = q.popleft()
        if board[x][y] == 3:
            return 1

        for i in range(4):
            dx, dy = x + direction[i][0], y + direction[i][1]
            if 0 <= dx < 100 and 0<= dy < 100:
                if not visited[dx][dy] and  board[dx][dy] != 1:
                    q.append((dx, dy))
                    visited[dx][dy] = 1

    return 0


for t in range(1, 11):
    print(f'#{t} {solution()}')
