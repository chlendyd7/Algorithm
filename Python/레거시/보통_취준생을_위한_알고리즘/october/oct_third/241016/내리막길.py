def dfs(x,y):
    if x == m - 1 and y == n - 1:
        return 1
    
    if dp[x][y] != -1:
        return dp[x][y]
    
    dp[x][y] = 0

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dx, dy in directions:
        nx, ny = x + dx, y + dy

        if 0<= nx < m and 0<= ny < n and graph[nx][ny] < graph[x][y]:
            dp[x][y] += dfs(nx, ny)

    return dp[x][y]

n,m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dp = [[-1] * n for _ in range(m)]
