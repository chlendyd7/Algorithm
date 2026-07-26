# https://school.programmers.co.kr/learn/courses/30/lessons/60063
from collections import deque

def get_next_pos(pos, board):
    next_pos = []
    pos = list(pos)
    x1, y1 = pos[0]
    x2, y2 = pos[1]
    
    dx = [-1,1,0,0]
    dy = [0,0,1,-1]
    for i in range(4):
        nx1, ny1 = x1 + dx[i], y1 + dy[i]
        nx2, ny2 = x2 + dx[i], y2 + dy[i]
        
        if board[nx1][ny1] == 0 and board[nx2][ny2]==0:
            next_pos.append({(nx1, ny1),(nx2, ny2)})
    
    if x1 == x2:
        for i in [-1, 1]:
            if board[x1+i][y1] == 0 and board[x2+i][y2] == 0:
                next_pos.append({(x1, y1), (x1+i, y1)})
                next_pos.append({(x2, y2), (x2+i, y2)})
    
    elif y1 == y2:
        for i in [-1,1]:
            if board[x1][y1+i] == 0 and board[x2][y2+i] == 0:
                next_pos.append({(x1, y1), (x1,y1+i)})
                next_pos.append({(x2, y2), (x2, y2+i)})
    
    return next_pos
    
    
def solution(board):
    
    n = len(board)
    new_board = [[1] * (n+2) for _ in range(n+2)]
    for i in range(n):
        for j in range(n):
            new_board[i+1][j+1] = board[i][j]
    
    pos = {(1,1), (1,2)}
    q = deque([(pos, 0)])
    visited = [pos]
    
    while q:
        curr_pos, cost = q.popleft()
        if (n,n) in curr_pos:
            return cost
        
        for next_p in get_next_pos(curr_pos, new_board):
            if next_p not in visited:
                visited.append(next_p)
                q.append((next_p, cost+1))
    
    return 0