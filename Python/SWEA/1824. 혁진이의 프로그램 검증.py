'''
- 현재 위치에 있는 문자가 나타내는 명령을 처리하고, 이동 방향에 따라 다음 문자로 이동해야 한다.
- 가장 처음 위치는 제일 왼쪽 위, 이동 방향은 오른쪽
- 만약 다음 이동이 2차원 격자의 바깥으로 이동하는 방향이면, 반대편에 있는 위치로 이동한다. 
- 메모리가 단 하나만 있으며 정수 하나만 저장 가능함
- 가장 처음은 0이 저장
'''
from collections import deque


direction = {
    'D': (1, 0),
    'R': (0, 1),
    'U': (-1, 0),
    'L': (0, -1)
}
huck = {
    '<': 'L',
    '>': 'R',
    '^': 'U',
    'v': 'D',
}

def solution():
    R, C = map(int, input().split())
    board = [list(input()) for _ in range(R)]

    memory = 0
    x, y = 0, 0
    direct = 'R'

    def dfs(x, y, direct):
        nonlocal memory
        char = board[x][y]
        
        if board[x][y] == '@':
            return 'YES'
        
        if char.isdecimal():
            memory = int(char)
            dx, dy = direction[direct]
            

    return 'NO'


T = int(input())
for t in range(1, T+1):
    print(f'#{t} {solution()}')