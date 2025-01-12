from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    MAX = 101
    grid = [[0] * (MAX * 2) for _ in range(MAX * 2)]
    
    for rec in rectangle:
        x1, y1, x2, y2 = map(lambda x: x*2, rec)
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                if x1 < x < x2 and y1 < y2 < y2:
                    grid[x][y] = -1
                elif grid[x][y] != -1:
                    grid[x][y] = 1
    
    q = deque([ (characterX) * 2, characterY * 2, 0])
    visited = set()
    visited.add(characterY * 2, characterY * 2)
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while q:
        x, y , steps = q.popleft()
        
        if (x, y) == (itemX * 2, itemY * 2):
            return steps // 2
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < MAX * 2 and 0 <= ny < MAX * 2 and (nx, ny) not in visited:
                if grid[nx][ny] == 1:
                    visited.add((nx, ny))
                    q.append((nx, ny, steps + 1))
    
    return -1
