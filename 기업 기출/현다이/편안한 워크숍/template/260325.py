import sys

INT_MAX = sys.maxsize
MAX_N = 100
MAX_K = 100
DIR_NUM = 4

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def find_min(i, j, l):
    if dp[i][j][l] != -1:
        return dp[i][j][l]


    if l == 1:
        dp[i][j][l] = 0
        return dp[i][j][l]

    best = INT_MAX
    dx = [-1,1,0,0]
    dy = [0,0,1,-1]
    for t in range(4):
        nx, ny = i + dx[t], j + dy[t]
        if in_range(nx,ny) and grid[nx][ny] > grid[i][j]:
            best = min(best, max(find_min(nx, ny, l, -1), grid[nx][ny] - grid[i][j]))
    
    dp[i][j][l] = best
    return dp[i][j][l]

n, k = tuple(map(int, input().split()))
grid = [list(map(int, input().split()))for _ in range(n)]

dp = [[[-1] * (MAX_K+1)]]

ans = INT_MAX
for i in range(n):
    for j in range(n):
        ans = min(ans, find_min(i,j,k))

if ans == INT_MAX:
    ans = -1

print(ans)