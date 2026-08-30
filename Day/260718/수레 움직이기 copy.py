from collections import deque
from itertools import product

direction = [(0,1), (1,0), (-1,0), (0,-1)]

def solution(maze):
    n, m = len(maze), len(maze[0])
    
    for i in range(n):
        for j in range(m):
            if maze[i][j] == 1: r = (i, j)
            elif maze[i][j] == 2: b = (i, j)
            elif maze[i][j] == 3: r_e = (i, j)
            elif maze[i][j] == 4: b_e = (i, j)
    
    q = deque()
    # state: (r위치, b위치, r_visited를 frozenset으로, b_visited를 frozenset으로, 턴)
    visited_states = set()
    
    r_visited = frozenset([(r[0], r[1])])
    b_visited = frozenset([(b[0], b[1])])
    state = (r, b, r_visited, b_visited)
    
    visited_states.add(state)
    q.append((r, b, r_visited, b_visited, 0))
    
    while q:
        r, b, r_visited, b_visited, cnt = q.popleft()
        
        if r == r_e and b == b_e:
            return cnt
        
        # r이 갈 수 있는 위치
        r_lst = []
        if r == r_e:
            r_lst.append(r)
        else:
            for dx, dy in direction:
                nx, ny = r[0] + dx, r[1] + dy
                if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] != 5:
                    if (nx, ny) not in r_visited:
                        r_lst.append((nx, ny))
        
        # b가 갈 수 있는 위치
        b_lst = []
        if b == b_e:
            b_lst.append(b)
        else:
            for dx, dy in direction:
                nx, ny = b[0] + dx, b[1] + dy
                if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] != 5:
                    if (nx, ny) not in b_visited:
                        b_lst.append((nx, ny))
        
        # 모든 이동 조합
        for rr, bb in product(r_lst, b_lst):
            if rr == bb: continue
            if rr == b and bb == r: continue
            
            new_r_visited = r_visited | frozenset([(rr[0], rr[1])])
            new_b_visited = b_visited | frozenset([(bb[0], bb[1])])
            new_state = (rr, bb, new_r_visited, new_b_visited)
            
            if new_state not in visited_states:
                visited_states.add(new_state)
                q.append((rr, bb, new_r_visited, new_b_visited, cnt + 1))
    
    return -1

print(solution([[1, 4], [0, 0], [2, 3]]))  # 3
print(solution([[1, 0, 2], [0, 0, 0], [5, 0, 5], [4, 0, 3]]))  # 7
