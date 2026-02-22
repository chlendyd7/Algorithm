from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

MAX = float('inf')

def solution(board):
    N = len(board)
    answer = 0
    visited = set()
    q = deque([(0,0,0,0)])


    while q:
        x, y, r, t = q.popleft()
        if (x, y) == (N-1, N-1) or (x + dx[r], y + dy[r]) == (N-1, N-1):
            answer = t
            break
        if (x, y, r) in visited or (x + dx[r], y + dy[r], (r+2) % 4) in visited:
            continue
        visited.add((x,y,r))
    
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if not 0 <= nx < N or 0 <= ny < N or board[nx][ny] == 1:
                continue
            _nx, _ny = nx + dx[r], ny + dy[r]
            if not 0 <= _nx < N or not 0 <= _ny < N or board[_nx][_ny] == 1:
                continue
            q.append((nx, ny, r, t+1))
    
        x, y, r = x + dx[r], y + dy[r], (r+2) % 4
        for i in [-1, 1]:
            _r = (r + i) % 4
            nx, ny = x + dx


    return answer
# 출처: https://magentino.tistory.com/35 [마젠티노's:티스토리]