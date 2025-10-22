from collections import deque


direction = [(1,0), (0,1), (-1,0), (0,-1)]

def solution(board):
    N = len(board)
    answer = 0
    visited = set()
    q = deque([0,0,0,0])
    
    while q:
        x, y, r, t = q.popleft()
        if (x, y) == (N-1, N-1) or \
            (x + direction[r][0], y + direction[r][1]) == (N-1, N-1):
                answer = t
                break
        if (x, y, r) in visited or \
            (x + direction[r][0], y + direction[r][1], (r+2) % 4) in visited:
                continue
    
        for dx, dy in direction:
            ax, ay = x + dx, y + dy
            if not -1 < ax < N or not -1 < ay < N or board[ax][ay] == 1:
                continue
            _ax, _ay = ax + dx[r], ay + dy[r]
            if not -1 < _ax < N or not -1 < _ay < N or board[ax][ay] == 1:
                continue
            q.append((ax, ay, r, t+1))
        
        x,y,r = x + dx[r], y + dy[r], (r+2) % 4
        for i in [-1, 1]:
            _r = (r + i) % 4
            