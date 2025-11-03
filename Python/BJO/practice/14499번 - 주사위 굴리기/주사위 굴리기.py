#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 14499                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: chlendyd7 <boj.kr/u/chlendyd7>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/14499                          #+#        #+#      #+#     #
#    Solved: 2025/11/03 20:54:58 by chlendyd7     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

'''
    N, M 크기
    N, M, 주사위 좌표 x, y, 명랭 개수 K
    
    2 ~ N개의 줄 북쪽 ~ 남쪽, 서쪽 ~ 동쪽
    
    이동하는 명령
'''

N,M,x,y,K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
commands = list(map(int, input().split()))

# 윗면, 아랫면, 북, 남, 서, 동
dice = [0, 0, 0, 0, 0, 0]

dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]

def roll(direction):
    top, bottom, north, south, west, east = dice

    if direction == 1:  # 동
        dice[0], dice[1], dice[4], dice[5] = west, east, bottom, top
    elif direction == 2:  # 서
        dice[0], dice[1], dice[4], dice[5] = east, west, top, bottom
    elif direction == 3:  # 북
        dice[0], dice[1], dice[2], dice[3] = south, north, top, bottom
    elif direction == 4:  # 남
        dice[0], dice[1], dice[2], dice[3] = north, south, bottom, top


for cmd in commands:
    nx = x + dx[cmd]
    ny = y + dy[cmd]
    
    if not (0 <= nx < N and 0 <= ny < M):
        continue
    
    x, y = nx, ny
    roll(cmd)
    
    if board[x][y] == 0:
        board[x][y] = dice[1]
    else:
        dice[1] = board[x][y]
        board[x][y] = 0
    
    print(dice[0])
