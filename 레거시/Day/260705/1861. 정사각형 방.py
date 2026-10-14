from collections import deque, defaultdict


def solution():
    def simulation(board):
        nonlocal r_x, r_y, total_mx
        for i in range(n):
            for j in range(n):
                q = deque([(i,j, 0)])
                mx = -1
                while q:
                    x, y, z = q.popleft()
                    print(x,y,z)
                    mx = max(mx, z)
                    for dx, dy in [(0,1), (1,0), (-1,0), (0,-1)]:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < n and 0 <= ny < n:
                            if board[nx][ny] == board[x][y] + 1:
                                q.append((nx,ny,z+1))
                if total_mx < mx:
                    r_x, r_y = i+1, j+1
                    total_mx = mx

    n = int(input())
    board = [list(map(int,input().split())) for _ in range(n)]
    r_x, r_y = -1, -1
    total_mx = 1
    simulation(board)
    
    return f"{board[i][j]} {total_mx}"
T = int(input())
for t in range(1, T + 1):
    print(f'#{t} {solution()}')
    
    

'''
캐시 사용
'''

direction = [
    (1, 0),
    (0, 1),
    (0, -1),
    (-1, 0)
]
def solution():
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    cache = [[0]*N for _ in range(N)]

    def dfs(x, y):
        if cache[x][y] != 0:
            return cache[x][y]

        max_len = 1
        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and board[nx][ny] == board[x][y] + 1:
                max_len = max(max_len, 1 + dfs(nx, ny))
        cache[x][y] = max_len
        return max_len

    max_move = 0
    min_start = float('inf')

    for i in range(N):
        for j in range(N):
            length = dfs(i, j)
            if length > max_move:
                max_move = length
                min_start = board[i][j]
            elif length == max_move:
                min_start = min(min_start, board[i][j])
    return f'{min_start} {max_move}'


T = int(input())
for t in range(1, T+1):
    print(f'#{t} {solution()}')
