import sys
input = sys.stdin.readline

def dfs(x,y):
    if x == M -1 and y == N -1:
        return 1
    if dp[x][y] != -1:
        return dp[x][y]
    
    dp[x][y] = 0
    direction = ((1,0),(-1,0),(0,1),(0,-1))
    for dx, dy in direction:
        nx, ny = x+dx, y+dy
        if 0<= nx < M and 0<= ny < N and lst[nx][ny] < lst[x][y]:
            dp[x][y] += dfs(nx,ny)
    return dp[x][y]
        








M, N = map(int, input().split())
lst = [list(map(int,input().split())) for _ in range(M)]
dp = [[-1] * N for _ in range(M)]
print(dfs(0,0))