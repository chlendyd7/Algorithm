from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def simulation(pos1, pos2, t, new_board):
    next_pos = []
    
    x1, y1 = pos1
    x2, y2 = pos2
    
    # 1. 상하좌우 이동
    for r in range(4):
        nx1, ny1 = x1 + dx[r], y1 + dy[r]
        nx2, ny2 = x2 + dx[r], y2 + dy[r]
        if new_board[nx1][ny1] != 1 and new_board[nx2][ny2] != 1:
            next_pos.append(((nx1, ny1), (nx2, ny2), t + 1))
    
    # 2. 가로 상태 회전 (x1 == x2)
    if x1 == x2:
        for r in [1, -1]:
            nx1, ny1 = x1 + r, y1
            nx2, ny2 = x2 + r, y2
            # 회전축 두 칸에서 회전하려는 방향(대각선 포함) 2칸 모두 빈칸(0)이어야 함
            if new_board[nx1][ny1] == 0 and new_board[nx2][ny2] == 0:
                # [수정] (x1, y1) 축으로 회전 -> (x1, y1)과 (x1+r, y1)
                next_pos.append(((x1, y1), (x1 + r, y1), t + 1))
                # [수정] (x2, y2) 축으로 회전 -> (x2, y2)과 (x2+r, y2)
                next_pos.append(((x2, y2), (x2 + r, y2), t + 1))
    
    # 3. 세로 상태 회전 (y1 == y2)
    elif y1 == y2:
        for r in [1, -1]:
            ny1, ny2 = y1 + r, y2 + r
            # [수정] y1+r, y2+r 방향으로 이동 가능 여부 체크
            if new_board[x1][ny1] == 0 and new_board[x2][ny2] == 0:
                # [수정] (x1, y1) 축으로 회전 -> (x1, y1)과 (x1, y1+r)
                next_pos.append(((x1, y1), (x1, y1 + r), t + 1))
                # [수정] (x2, y2) 축으로 회전 -> (x2, y2)과 (x2, y2+r)
                next_pos.append(((x2, y2), (x2, y2 + r), t + 1))
    
    return next_pos


def solution(board):
    n = len(board)
    m = len(board[0])
    
    # [수정] 인덱스 초과(IndexError) 방지를 위해 패딩을 상하좌우 모두 (+2) 해줘야 함
    new_board = [[1] * (m + 2) for _ in range(n + 2)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            new_board[i][j] = board[i - 1][j - 1]
    
    visited = set()
    q = deque()
    q.append(((1, 1), (1, 2), 0))
    
    while q:
        pos1, pos2, t = q.popleft()
        
        # (N, M) 위치 도달 확인
        if pos1 == (n, m) or pos2 == (n, m):
            return t
        
        # [수정] ((1,1), (1,2))와 ((1,2), (1,1))은 같은 상태이므로 sorted로 정렬하여 방문 체크
        state = tuple(sorted([pos1, pos2]))
        
        if state in visited:
            continue
        visited.add(state)
        
        q.extend(simulation(pos1, pos2, t, new_board))
        
    return 0