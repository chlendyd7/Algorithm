direction = [
    (0,1),
    (1,0),
    (0, -1),
    (-1, 0)
]

def snail(n):
    board = [[0] * n for _ in range(n)]
    row, col, d = 0, 0, 0

    for num in range(1, n*n + 1):
        board[row][col] = num
        dr, dc = direction[d]
        nr, nc = row + dr, col + dc

        if not(0 <= nr < n and 0 <= nc < n) or board[nr][nc]:
            d = (d + 1) % 4
            dr, dc = direction[d]
            nr, nc = row + dr, col + dc
        
        row, col = nr, nc
    
    return board

T = int(input())
for t in range(1, T+1):
    n = int(input())
    board = snail(n)
    print(f'#{t}')
    for row in board:
        print(' '.join(map(str, row)))

# def snail(n):
#     board = [[0] * n for _ in range(n)]
#     directions = [(0,1), (1,0), (0,-1), (-1,0)]  # → ↓ ← ↑
#     row = col = d = 0  # 시작 위치, 방향 인덱스
#     for num in range(1, n*n + 1):
#         board[row][col] = num
#         dr, dc = directions[d]
#         nr, nc = row + dr, col + dc

#         # 범위 벗어나거나 이미 채워졌다면 방향 바꿔
#         if not (0 <= nr < n and 0 <= nc < n) or board[nr][nc]:
#             d = (d + 1) % 4
#             dr, dc = directions[d]
#             nr, nc = row + dr, col + dc

#         row, col = nr, nc

#     return board