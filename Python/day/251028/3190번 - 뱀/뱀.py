#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 3190                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: chlendyd7 <boj.kr/u/chlendyd7>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/3190                           #+#        #+#      #+#     #
#    Solved: 2025/10/28 21:48:01 by chlendyd7     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

from collections import deque

directions = [(0,1), (1,0), (0,-1), (-1,0)]
RIGHT, LEFT = 'D', 'L'

N = int(input())
K = int(input())
board = [[0] * N for _ in range(N)]

apples = []
for _ in range(K):
    r, c = map(int, input().split())
    apples.append((r,c))

L = int(input())
cmd_key = {}
for _ in range(L):
    inputs = input().split()
    num = int(inputs[0])
    cmd = inputs[1]
    cmd_key[num] = cmd

snake = deque([(0,0)])
snake_set = {(0,0)}
direction = 0
time = 0

while True:
    time += 1
    dr, dc = directions[direction]
    head_r, head_c = snake[-1]
    nr, nc = head_r + dr, head_c + dc

    if not(0 <= nr < N and 0<= nc < N) or (nr, nc) in snake_set:
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
            direction = (direction + 1) % 4
        else:
            direction = (direction - 1) % 4

print(time)