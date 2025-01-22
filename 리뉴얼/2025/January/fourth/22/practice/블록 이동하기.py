from collections import deque


direction = [(1,0), (0,1), (-1,0), (0,-1)]

def solution(board):
    N = len(board)
    visited = set()
    q = deque([(0,0,0,0)])

    while q:
        x, y, r, t = q.popleft()
        if (x, y) == (N-1, N-1) or (x + direction[r][0], y + direction[r][1]) == (N-1, N-1):
            return t
        if (x, y, r) in visited or (x + direction[r][0], y + direction[r][1], (r+2) % 4) in visited:
            continue
        visited.add((x,y,r))

        for i in range(4):
            ax, ay = x + direction[i][0], y + direction[i][1]
            if not -1 < ax < N or not -1 < ay < N or board[ay][ax] == 1:
                continue
            _ax, _ay = ax + direction[r][0], ay + direction[r][1]
            if not -1 < _ax < N or not -1 < _ay < N or board[_ay][_ax] == 1:
                continue
            q.append((ax, ay, r, t+1))

        x,y,r = x + direction[r][0], y + direction[r][1], (r+2) % 4
        for i in [-1, 1]:
            _r = (r + i) % 4
            ax, ay = x + direction[_r][0], y + direction[_r][1]
            if not -1 < ax < N or not -1 < ay < N or board[ay][ax] == 1:
                continue
            cx, cy = ax + direction[r][0], ay + direction[r][1]
            if board[cy][cx] == 1:
                continue
            q.append((x,y,_r,t+1))

    return 0

solution([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]])