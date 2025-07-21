def rotate(board):
    rotated = [[0] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            rotated[c][N -1- r] = board[r][c]
    return rotated

def get_rotations(board):
    rot90 = rotate(board)
    rot180 = rotate(rot90)
    rot270 = rotate(rot180)
    return rot90, rot180, rot270

def format_row(row):
    return ''.join(map(str, row))

T = int(input())
for t in range(1, T+1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    rot90, rot180, rot270 = get_rotations(board)
    print(f'#{t}')
    for i in range(N):
        print(f"{format_row(rot90[i])} {format_row(rot180[i])} {format_row(rot270[i])}")
