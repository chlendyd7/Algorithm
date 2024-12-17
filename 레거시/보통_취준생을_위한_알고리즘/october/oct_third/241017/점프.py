def dfs(x,y):
    if x == n -1 and y == n -1:
        return 1

    if dp[x][y] != -1:
        return dp[x][y]

    dp[x][y] = 0
    directions = [(1,0),(0,1)]
    for dx, dy in directions:
        nx, ny = x + (graph[x][y] * dx), y + (graph[x][y] * dy)
        if 0<= nx < n and 0<= ny < n:
            dp[x][y] += dfs(nx,ny)
    
    return dp[x][y]


n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1] * n for _ in range(n)]

print(dfs(0,0))
