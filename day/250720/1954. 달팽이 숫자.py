direction = [
    (0, 1),
    (1, 0),
    (0, -1),
    (-1, 0)
]
def snail(n):
    matrix = [[0] * n for _ in range(n)]
    row, col, d = 0, 0, 0

    for num in range(1, n*n + 1):
        matrix[row][col] = num
        dx, dy = direction[d]
        nr, nc = row + dx, col + dy

        if not(0 <= nr < n and 0<= nc < n) or matrix[nr][nc]:
            d = (d + 1) % 4
            dr, dc = direction[d]
            nr, nc = row + dr, col + dc
        
        row, col = nr, nc
    
    return matrix

T = int(input())
for t in range(1, T+1):
    n = int(input())
    board = snail(n)
    print(f'#{t}')
    for row in board:
        print(' '.join(map(str, row)))
