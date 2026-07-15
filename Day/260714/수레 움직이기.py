from itertools import product


def solution(maze):
    n,m = len(maze), len(maze[0])
    for i in range(n):
        for j in range(m):
            if maze[i][j] == 1: red = i,j
            elif maze[i][j] == 2: blue = i,j
            elif maze[i][j] == 3: red_end = i,j
            elif maze[i][j] == 4: blue_end = i,j
    
    r_visited = [[0] * m for _ in range(n)]
    b_visited = [[0] * m for _ in range(n)]
    directions = [(0,1), (1,0), (-1,0), (0,-1)]
    answer = 1e9

    def dfs(r, b, cnt):
        nonlocal answer
        if cnt >= answer:
            return
        if r == red_end and b == blue_end:
            answer = min(answer, cnt)
            return
        
        r_next = []
        if r == red_end:
            r_next.append(red_end)
        else:
            for dx, dy in directions:
                nr, nc = dx+r[0], dy+r[1]
                if 0 <= nr < n and 0 <= nc < m:
                    if maze[nr][nc] != 5 and r_visited[nr][nc] == 0:
                        r_next.append((nr,nc))
        
        b_next = []
        if b == blue_end:
            b_next.append(blue_end)
        else:
            for dx, dy in directions:
                nr, nc = dx+b[0], dy+b[1]
                if 0 <= nr < n and 0 <= nc < m:
                    if maze[nr][nc] != 5 and b_visited[nr][nc] == 0:
                        b_next.append((nr,nc))

        for nr, nb in product(r_next, b_next):
            if nr == nb: continue
            if nr == b and nb == r: continue
            r_moved = (r!=red_end)
            b_moved = (b!=blue_end)

            if r_moved: r_visited[nr[0]][nr[1]] = True

    r_visited[red[0]][red[1]] = 1  # ← 추가 필요
    b_visited[blue[0]][blue[1]] = 1  # ← 추가 필요

    dfs(red, blue, 0)
    return answer if answer != 1e9 else 0

print(solution([[1, 0, 2], [0, 0, 0], [5, 0 ,5], [4, 0, 3]]))






# 좋은 풀이

from itertools import product
def solution(maze):
    n, m =len(maze), len(maze[0])
    directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    
    for i in range(n):
        for j in range(m):
            if maze[i][j] == 1: r_start = (i, j)
            elif maze[i][j] == 2: b_start = (i, j)
            elif maze[i][j] == 3: r_end = (i, j)
            elif maze[i][j] == 4: b_end = (i, j)
    
    r_visited = [[False] * m for _ in range(n)]
    b_visited = [[False] * m for _ in range(n)]

    r_visited[r_start[0]][r_start[1]] = True
    b_visited[b_start[0]][b_start[1]] = True
    
    def get_next_positions(curr, end, visited):
        if curr == end:
            return [curr]
    
        next_steps = []
        cx, cy = curr
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] != 5 and not visited[nx][ny]:
                next_steps.append((nx,ny))
        return next_steps
    answer = float('inf')
    def dfs(r, b, cnt):
        nonlocal answer
        if cnt >= answer: return
        if r == r_end and b == b_end:
            answer = min(cnt, answer)
            return
        
        r_candidates = get_next_positions(r, r_end, r_visited)
        b_candidates = get_next_positions(b, b_end, b_visited)
        
        for nr, nb in product(r_candidates, b_candidates):
            if nr == nb: continue
            if nr == b and nb == r: continue
            
            r_moved = (r != r_end)
            b_moved = (b != b_end)
            
            if r_moved: r_visited[nr[0]][nr[1]] = True
            if b_moved: b_visited[nb[0]][nb[1]] = True
            
            dfs(nr, nb, cnt+1)
            
            if r_moved: r_visited[nr[0]][nr[1]] = False
            if b_moved: b_visited[nb[0]][nb[1]] = False
    
    dfs(r_start, b_start, 0)
    
    return answer if answer != float('inf') else 0