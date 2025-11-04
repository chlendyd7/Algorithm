#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 14503                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: chlendyd7 <boj.kr/u/chlendyd7>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/14503                          #+#        #+#      #+#     #
#    Solved: 2025/11/03 21:43:39 by chlendyd7     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
'''
    현재 칸 청소
    양옆 4칸 다 청소 됬으면 후진하기
    아니면 반시계방향 90도
    청소되지 않은 곳이 앞이면 한 칸 전진
    
    0은 청소되지 않음
    1은 벽
    두번 째 좌표와 로봇 청소기가 바라보느 방향
'''
from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

N, M = map(int, input().split())
r,c,d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

x, y = r, c
cnt = 0
while True:
    if board[r][c] == 0:
        board[r][c] = 2
        cnt += 1

    moved = False
    for i in range(4):
        d = (d + 3) % 4
        nx, ny = r + dx[d], c + dy[d]
        if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == 0:
            r, c = nx, ny
            moved = True
            break
    if moved:
        continue

    bx, by = r - dx[d], c - dy[d]
    if not (0 <= bx < N and 0 <= by < M) or board[bx][by] == 1:
        break
    r, c = bx, by

print(cnt)

# q = deque([(r,c)])
# cnt = 0
# while q:
#     x, y = q.popleft()
    
#     if board[x][y] == 0:
#         cnt += 1
#         board[x][y] = 1
    