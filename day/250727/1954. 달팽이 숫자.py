direction = (
    (0, 1),
    (1, 0),
    (0, -1),
    (-1, 0),
)
def solution():
    n = int(input())
    board = [[0] * n for _ in range(n)]
    x, y, d = 0, 0, 0
    for num in range(1, n**2 + 1):
        board[x][y] = num
        nx, ny = direction[d]
        dx, dy = x + nx, y + ny
        if not (0 <= dx < n and 0 <= dy < n) or board[dx][dy]:
            d = (d + 1) % 4
            nx, ny = direction[d]

        x, y = x + nx, y + ny

    return board


T = int(input())
for t in range(1, T+1):
    board = solution()
    print(f'#{t}')
    for row in board:
        print(' '.join(map(str, row)))

