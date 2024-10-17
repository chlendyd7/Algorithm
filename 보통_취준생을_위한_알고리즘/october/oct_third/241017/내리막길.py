m,n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(m)]
dp = [[-1] * n for _ in range(m)]

def dfs(x,y):
    if x == m -1 and y == n - 1:
        return 1
    
    if dp[x][y] != -1:
        return dp[x][y]
    
    dp[x][y] = 0
    direction = [(-1,0), (1,0), (0,1), (0,-1)]

    for dx, dy in direction:
        nx, ny = x + dx, y + dy

        if 0<= nx < m and 0<= ny < n and graph[nx][ny] < graph[x][y]:
            dp[x][y] += dfs(nx, ny)
    
    return dp[x][y]

print(dfs(0,0))

