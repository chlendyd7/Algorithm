'''
- N^2개의 방이 N x N
- 숫자 범위: 1이상 N^2이하
- 상하좌우 이동
- 이동하려는 방이 현재 방에 적힌 숫자보다 정확히 1 더 커야함
- 처음 어떤 수가 적힌 방에 있어야 가장 많은 개수의 방을 이동할 수 있는지 구하라
'''
from collections import deque

direction = [
    (1, 0),
    (0, 1),
    (0, -1),
    (-1, 0)
]
def solution():
    N = int(input())
    board = []
    for _ in range(N):
        board.append(list(map(int, input().split())))

    def bfs(x, y):
        q = deque()
        q.append((x,y))
        cnt = 0
        while q:
            x, y = q.popleft()
            cnt += 1
            for dx, dy in direction:
                if 0 <= x + dx < N and 0 <= y + dy < N \
                    and board[x + dx][y + dy] == board[x][y] + 1:
                        q.append((x + dx, y + dy))

        return cnt

    mx_list = []
    mx = 0

    for i in range(N):
        for j in range(N):
            if bfs(i, j) > mx:
                mx_list = [board[i][j]]
                mx = bfs(i,j)
            elif bfs(i, j) == mx:
                mx_list.append(board[i][j])
    print(mx_list)
    return f'{min(mx_list)} {mx}'


T = int(input())
for t in range(1, T+1):
    print(f'#{t} {solution()}')
