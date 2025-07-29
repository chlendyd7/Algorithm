direction = [
    (1, 0),
    (0, 1),
    (-1, 0),
    (0, -1)
]
def solution():
    board = [list(map(int, input().split())) for _ in range(4)]
    num_set = set()

    def dfs(x, y, depth, string):
        if depth == 6:
            num_set.add(string)
            return

        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 4 and 0 <= ny < 4:
                dfs(nx, ny, depth + 1, string + str(board[nx][ny]))

    for i in range(4):
        for j in range(4):
            dfs(i, j, 0, str(board[i][j]))

    return len(num_set)


T = int(input())
for t in range(1, T+1):
    print(f'#{t} {solution()}')