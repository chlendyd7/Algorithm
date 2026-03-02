from functools import cache


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
RIGHT, DOWN, DAGAK = 1, 2, 3

def check(r, c, shape):
    if shape == RIGHT:
        return c + 1 < N and board[r][c + 1] == 0
    elif shape == DOWN:
        return r + 1 < N and board[r + 1][c] == 0
    elif shape == DAGAK:
        if r + 1 < N and c + 1 < N:
            return board[r+1][c] == 0 and board[r][c+1] == 0 and board[r+1][c+1] == 0
    return False

@cache
def dfs(r,c,shape):
    if r == N-1 and c == N-1:
        return 1
    
    cnt = 0
    if shape == RIGHT or shape == DAGAK:
        if check(r, c, RIGHT):
            cnt += dfs(r, c+1, RIGHT)
    
    if shape == DOWN or shape == DAGAK:
        if check(r, c, DOWN):
            cnt += dfs(r+1, c, DOWN)
    if check(r, c, DAGAK):
        cnt += dfs(r+1, c+1, DAGAK)

    return cnt

print(dfs(0,1,RIGHT))
