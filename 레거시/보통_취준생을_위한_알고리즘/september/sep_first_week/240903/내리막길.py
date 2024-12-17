def dfs(y, x):
    if dp[y][x] != -1:
        return dp[y][x]
    if y == m-1 and x == n-1:
        return 1
    
    dp[y][x] = 0
    for i in range(4):
        yy = y + dy[i]
        xx = x + dx[i]
        if 0 <= yy < m and 0 <= xx < n and lst[y][x] > lst[yy][xx]:
            dp[y][x] += dfs(yy, xx)
    
    return dp[y][x]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


m,n = map(int,input().split())
dp = [[-1] * n for _ in range(m)]
lst = [list(map(int,input().split())) for _ in range(m)]

print(dfs(0,0))
