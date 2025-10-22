def dfs(row, value):
    global min_value

    if value >= min_value:
        return

    if row == n:
        min_value = min(min_value, value)
        return 

    for i in range(n):
        if not matrix[i]:
            matrix[i] = True
            dfs(row + 1, value + board[row][i])
            matrix[i] = False


T = int(input())
for t in range(1, T+1):
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    matrix = [False] * n
    min_value = 1e9
    dfs(0, 0)
    print(f'#{t} {min_value}')
