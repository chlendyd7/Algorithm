from collections import deque


def solution(maps):
    rows, cols = len(maps), len(maps[0])
    start, lever, exit = None, None, None
    for r in range(rows):
        for c in range(cols):
            if maps[r][c] == 'S':
                start = (r, c)
            elif maps[r][c] == 'L':
                lever = (r, c)
            elif maps[r][c] == 'E':
                exit = (r, c)
    
    def bfs(start, target):
        q = deque([(start[0], start[1], 0)])
        visited = [[False] * cols for _ in range(rows)]
        visited[start[0]][start[1]] = True

        directions = [(-1, 0), (1,0), (0, -1), (0, 1)]
        
