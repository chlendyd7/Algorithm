from collections import deque

direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def bfs(h, w, i, j, maps, visited):
    cnt = 0
    q = deque()
    q.append((i, j))
    visited[i][j] = True  # 방문 처리
    
    while q:
        x, y = q.popleft()
        cnt += int(maps[x][y])  # 현재 위치의 값을 합산
        
        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny] and maps[nx][ny] != 'X':
                visited[nx][ny] = True  # 방문 처리
                q.append((nx, ny))
                
    return cnt

def solution(maps):
    h, w = len(maps), len(maps[0])
    visited = [[False] * w for _ in range(h)]  # 수정: 크기 변경
    answer = []
    
    for i in range(h):
        for j in range(w):
            if maps[i][j] != 'X' and not visited[i][j]:
                answer.append(bfs(h, w, i, j, maps, visited))
    
    if answer:
        return sorted(answer)  # 수정: sorted로 정렬 후 반환
    else:
        return [-1]
