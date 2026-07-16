# https://school.programmers.co.kr/learn/courses/30/lessons/250134
'''
    n,m 크기의 퍼즐판
    자신의 칸에서 도착 칸 까지 이동해야함
    
    필요한 턴의 최솟값을 return 하여라
    4x4면 완탐, 백트래킹
    
    빨강이 먼저 움직이냐 파랑이 먼저 움직이냐 빽 트래킹 계속
    maze 계속 만들기
    
    도착하면 움직이지 않음
    방문했던 칸 x, r_visited, b_visited
    두 수레 같은 칸 x
    자리 바꾸기 x
    
    1빨강 -> 3
    2파랑 -> 4
    
    r먼저 이동, b 이동 근데 각각 달라야함
    for문 dx dy?면 무조건 같은 방향이여서 안됨
    움직였던 곳 len을 가져가면 되지 않을까?
    근데 그럼 같이 데리고 다녀야하나?
    반대로도 수행해야함

    maze를 두고
    visited도 방문했을 경우 분기 처리 길이로 비교하게 된다면..

'''

direction = [(0,1), (1,0), (-1,0), (0,-1)]
def solution(maze):
    n, m = len(maze), len(maze[0])
    r_s, b_s = None, None
    r_e, b_e = None, None
    n, m = len(maze), len(maze[0])
    for i in range(n):
        for j in range(m):
            if maze[i][j] == 1:
                r = i, j
            elif maze[i][j] == 2:
                b = i, j
            elif maze[i][j] == 3:
                r_e = (i,j)
            elif maze[i][j] == 4:
                b_e = (i, j)
    answer = float('inf')
    
    r_visited = {r_s}
    b_visited = {b_s}

    def dfs(r, b, cnt):
        nonlocal answer
        
        if cnt >= answer:
            return
        
        if r == r_e and b == b_e:
            answer = min(answer, cnt)
            return
    
        r_next = []
        if r == r_e:
            r_next.append(r)
        else:
            for dx, dy in direction:
                nrx, nry = r[0] + dx, r[1] + dy
                if 0 <= nrx < n and 0 <= nry < m and maze[nrx][nry] != 5:
                    if (nrx, nry) not in r_visited:
                        r_next.append((nrx, nry))
        
        b_next = []
        if b == b_e:
            b_next.append(b)
        else:
            for dx, dy in direction:
                nbx, nby = b[0] + dx, b[1] + dy
                if 0 <= nbx < n and 0 <= nby < m and maze[nbx][nby] != 5:
                    if (nbx, nby) not in b_visited:
                        b_next.append((nbx, nby))
        
        for nr in r_next:
            for nb in b_next:
                if nr == nb:
                    continue
                if nr == b and nb == r:
                    continue
                
                r_has_moved = (r!=r_e)
                b_has_moved = (b!=b_e)
                if r_has_moved: r_visited.add(nr)
                if b_has_moved: b_visited.add(nb)
                
                dfs(nr, nb, cnt + 1)
                
                if r_has_moved: r_visited.remove(nr)
                if b_has_moved: b_visited.remove(nb)
    dfs(r_s, b_s, 0)
        
    return answer if answer != float('inf') else 0





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