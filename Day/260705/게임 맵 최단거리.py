from collections import deque
def solution(maps):
    n,m = len(maps), len(maps[0])
    answer = 0
    q = deque([(0,0,1)])
    visited = [[0] * m for _ in range(n)]
    visited[0][0] = 1
    while q:
        x, y, z = q.popleft()
        if x == n-1 and y == m-1:
            return z
        
        for dx, dy in [(0,1), (1,0), (0,-1), (-1,0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:
                if visited[nx][ny] == 0 and maps[nx][ny] == 1:
                    q.append((nx,ny,z+1))
                    visited[nx][ny] = 1
        
    return -1
