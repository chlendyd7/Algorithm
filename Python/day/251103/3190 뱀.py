from collections import deque


directions = [(0,1), (1,0), (0,-1), (-1,0)]
RIGHT, LEFT = 'D', 'L'

N = int(input())
K = int(input())
board =[[0] * N for _ in range(N)]

for _ in range(K):
    r, c = map(int, input().split())
    board[r-1][c-1] = 1

L = int(input())
cmd = {}
for _ in range(L):
    t, d = input().split()
    cmd[int(t)] = d

snake = deque([(0,0)])
snake_set = {(0,0)}
d = 0
time = 0

while True:
    time += 1
    dr, dc = directions[d]
    head_r, head_c = snake[-1]
    nr, nc = head_r + dr, head_c + dc
    
    if not(0 <= nr < N and 0 <= nc < N) or (nr, nc) in snake_set:
        break
    
    snake.append((nr, nc))
    snake_set.add((nr, nc))
    
    if board[nr][nc] == 1:
        board[nr][nc] = 0
    else:
        tail = snake.popleft()
        snake_set.remove(tail)
    
    if time in cmd:
        if cmd[time] == RIGHT:
            d = (d + 1) % 4
        else:
            d = (d - 1) % 4
