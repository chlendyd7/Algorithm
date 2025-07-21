direction = [
    (0, 1),
    (1, 0),
    (0, -1),
    (-1, 0)
]

def solution(n):
    board = [[0] * n for _ in range(n)]
    r, c, d = 0, 0, 0
    for num in range(1, n*n + 1):
        board[r][c] = num
        dr, dc = direction[d]
        nr, nc = r + dr, c + dc

        if not (0 <= nr < n and 0 <= nc < n) or board[nr][nc]:
            d = (d + 1) % 4
            dr, dc = direction[d]
            nr, nc = r + dr, c + dc

        r, c = nr, nc

    return board

T = int(input())
for t in range(1, T+1):
    print(f'#{t}')
    n = int(input())
    board = solution(n)
    print(board)
    # for i in range(n):
    #     print(''.join(board[i]))
