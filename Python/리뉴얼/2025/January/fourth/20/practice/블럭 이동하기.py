from collections import deque

# 상, 우, 하, 좌
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def is_valid(x, y, N, board):
    return 0 <= x < N and 0 <= y < N and board[y][x] == 0

def solution(board):
    N = len(board)
    visited = set()
    q = deque([(0,0,0,0)])
    answer = 0

    while q:
        x, y, r, t = q.popleft()

        if (x, y) == (N-1, N-1) or (x + dx[r], y + dy[r]) == (N-1, N-1):
            return t
        if(x, y, r) in visited or (x + dx[r], y +dy[r], (r+2) % 4) in visited:
            continue
        visited.add((x,y,r))
        
        for i in range(4):
            ax, ay = x + dx[i], y + dy[i]
            if not -1 < ax < N or not -1 < ay < N or board[ay][ax] == 1:
                continue
            _ax, _ay = ax + dx[r], ay + dy[r]
            if not -1 < _ax < N or not -1 < _ay < N or board[_ay][_ax] == 1:
                continue
            q.append((ax, ay, r, t+1))
        
        x,y,r = x + dx[r], y + dy[r], (r+2) % 4
        for i in [-1, 1]:
            _r = (r + i) % 4
            ax, ay = x + dx[_r], y + dy[_r]
            if not -1 < ax <N or not -1 < ay < N or board[ay][ax] == 1:
                continue
            cx, cy = ax + dx[r], ay + dy[r]
            if board[cy][cx] == 1:
                continue
            q.append((x,y,_r, t+1))
            
    return answer
