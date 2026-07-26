# https://school.programmers.co.kr/learn/courses/30/lessons/60063

from collections import deque

def get_next_pos(pos, board):
    next_pos = []
    pos = list(pos) # 현재 로봇이 차지하는 두 칸 좌표 [(x1, y1), (x2, y2)]
    x1, y1 = pos[0]
    x2, y2 = pos[1]
    
    # 1. 상, 하, 좌, 우 평행 이동
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(4):
        nx1, ny1 = x1 + dx[i], y1 + dy[i]
        nx2, ny2 = x2 + dx[i], y2 + dy[i]
        # 이동할 두 칸이 모두 빈칸(0)이면 가능
        if board[nx1][ny1] == 0 and board[nx2][ny2] == 0:
            next_pos.append({(nx1, ny1), (nx2, ny2)})
            
    # 2. 회전 이동
    # 가로로 놓여있는 경우 (y좌표가 다르고 x좌표가 같음)
    if x1 == x2:
        for i in [-1, 1]: # 위쪽(-1) 또는 아래쪽(1)으로 회전
            # 회전하려는 방향의 두 칸이 모두 빈칸이어야 회전 가능 (대각선 체크 포함)
            if board[x1 + i][y1] == 0 and board[x2 + i][y2] == 0:
                next_pos.append({(x1, y1), (x1 + i, y1)})
                next_pos.append({(x2, y2), (x2 + i, y2)})
                
    # 세로로 놓여있는 경우 (x좌표가 다르고 y좌표가 같음)
    elif y1 == y2:
        for i in [-1, 1]: # 왼쪽(-1) 또는 오른쪽(1)으로 회전
            # 회전하려는 방향의 두 칸이 모두 빈칸이어야 회전 가능 (대각선 체크 포함)
            if board[x1][y1 + i] == 0 and board[x2][y2 + i] == 0:
                next_pos.append({(x1, y1), (x1, y1 + i)})
                next_pos.append({(x2, y2), (x2, y2 + i)})
                
    return next_pos

def solution(board):
    n = len(board)
    
    # 맵 외곽을 벽(1)으로 두르는 패딩(Padding) 작업 (경계 조건 체크 단순화)
    new_board = [[1] * (n + 2) for _ in range(n + 2)]
    for i in range(n):
        for j in range(n):
            new_board[i + 1][j + 1] = board[i][j]
            
    # 시작 상태 설정 (1,1)과 (1,2)
    pos = {(1, 1), (1, 2)}
    q = deque([(pos, 0)]) # (현재 로봇 위치 set, 경과 시간)
    visited = [pos]
    
    while q:
        curr_pos, cost = q.popleft()
        
        # 목적지 (N, N)에 도달했는지 확인
        if (n, n) in curr_pos:
            return cost
        
        # 이동 가능한 다음 위치 탐색
        for next_p in get_next_pos(curr_pos, new_board):
            if next_p not in visited:
                visited.append(next_p)
                q.append((next_p, cost + 1))
                
    return 0