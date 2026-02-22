'''
궁금한점
1. max memmory
2. 재귀 return
3. im sw 역량테스트 대비 보충 1차 들을만한가 a 형
'''
direction = [
    (0, 1),
    (0, -1),
    (1, 0)
]

def solution():
    _ = input()
    board = [list(map(int, input().split())) for _ in range(100)]

    def dfs(x, y, visited):
        if board[x][y] == 2:
            return True

        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 100 and 0 <= ny < 100 and \
                board[nx][ny] != 0 and not visited[nx][ny]:
                visited[nx][ny] = 1
                if dfs(nx, ny, visited):
                    return True
        return False

    for i in range(100):
        visited = [[0] * 100 for _ in range(100)]
        if board[0][i] == 1:
            visited[0][i] = 1
            if dfs(0, i, visited):
                print("???")
                return i


for t in range(1, 11):
    print(f'#{t} {solution()}')