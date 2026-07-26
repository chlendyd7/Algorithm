def rotate_90(grid, N):
    new_grid = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            new_grid[j][N-1-i] = grid[i][j]
    return new_grid


def rotate_180(grid):
    N, M = len(grid), len(grid[0])
    new_grid = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            new_grid[N-1-i][M-1-j] = grid[i][j]
    return new_grid

def rotate_270(grid):
    N, M = len(grid), len(grid[0])
    new_grid = [[0] * M for _ in range(N)]
    for i in range(N):
            for j in range(M):
                new_grid[M-1-j][i] = grid[i][j]
    return new_grid



# j N-1-i
# N-1-i, M-1-i
# M-1-j, i