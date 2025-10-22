from collections import deque
dx = [-1,0,1,0]
dy = [0,1,0,-1]

def direction_change(d, c):
    if c == 'L':
        d = (d - 1) % 4
    else:
        d = (d + 1) % 4
    return d


n = int(input())
board = [[0] * n for _ in range(n)]

k = int(input())
for _ in range(k):
    x,y = map(int,input().split())
    board[x-1][y-1] = 1

L = int(input())
times = {}
for i in range(L):
    x, c = input().split()
    times[int(x)] = c

direction = 1
time = 1
y, x = 0, 0
snake = deque([[y,x]])
board[y][x] = 2

while True:
    y, x = y + dy[direction], x + dx[direction]
    if 0 <= y < n and 0 <= x < n and board[y][x] != 2:
        if not board[y][x] == 1:
            delY, delX = snake.popleft()
            board[delY][delX] = 0
        board[y][x] = 2
        snake.append([y, x])
        if time in times.keys():
            direction = direction_change(direction, times[time])
        time += 1
    else:
        break

print(time)