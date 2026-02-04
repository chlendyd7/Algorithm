
while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    matrix = [list(map(int, input().split())) for _ in range(n)]
    dp = [[0] * (n+1) for _ in range(m+1)]
    result = 0
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 1:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                result = max(result, dp[i][j])
    print(result)
