import sys


N, M = map(int, input().split())
board = [list(input()) for _ in range(3)]
check = False
combo = set()
direction = [(0,1), (1,0), (0,-1), (-1,0)]

def dfs(visited:list, x, y):
    global check
    if len(visited) ==M*2 - 1:
        temp = 0
        minus = False
        for x, y in visited:
            if board[x][y].isdigit():
                nums = int(board[x][y])
                if minus:
                    nums = nums * -1
                    minus = False
                temp += nums
            else:
                if board[x][y] == '+':
                    continue
                else:
                    minus = True
        if temp == N:
            print(1)
            check = True
            for x, y in visited:
                print(x, y)
            sys.exit(0)
        return

    for dx, dy in direction:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            if (nx,ny) not in visited:
                visited.append((nx, ny))
                dfs(visited, nx, ny)
                visited.pop()


start = [
    (0,0), (0,2), (1,1), (2,0), (2,2)
]
for x, y in start:
    dfs([(x,y)], x, y)

print(0)
