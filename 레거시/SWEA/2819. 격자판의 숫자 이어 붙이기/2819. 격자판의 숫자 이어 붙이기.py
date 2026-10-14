DIRECTION = [
    (0,1),
    (1,0),
    (-1,0),
    (0,-1)
]
N = 4
T = int(input())
def dfs(n, r, c, string):
    if n >= 6:
        num_set.add(string)
        return

    for dx, dy in DIRECTION:
        nr, nc = r + dx, c + dy
        if nr < 0 or nr >= N or nc < 0 or nc >= N:
            continue
        dfs(n+1, nr, nc, string+board[nr][nc])

for tc in range(1, T+1):
    num_set = set()
    board = [list(input().split()) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            dfs(0, i, j, board[i][j])
    print(f'#{tc} {len(num_set)}')
