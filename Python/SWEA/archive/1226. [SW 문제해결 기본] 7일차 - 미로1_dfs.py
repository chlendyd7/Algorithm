direction = [
    (1,0),
    (0,1),
    (-1,0),
    (0,-1)
]

def solution():
    N = int(input())
    board = [list(map(int, input())) for _ in range(16)]
    visited = [[0] * 16 for _ in range(16)]
    visited[1][1] = 1
    check = False

    def dfs(r, c):
        nonlocal check
        if board[r][c] == 3:
            # check = True
            return True
        
        for dr, dc in direction:
            nr, nc = r + dr, c + dc
            if 0 <= nr < 16 and 0 <= nc < 16:
                if not visited[nr][nc] and board[nr][nc] != 1:
                    visited[nr][nc] = 1
                    if dfs(nr, nc):
                        return True
                    visited[nr][nc] = 0

        return False


    return dfs(1,1)
    # return 1 if check else 0


for t in range(1, 11):
    check = solution()
    print(f'#{t} {1 if check else 0}')

