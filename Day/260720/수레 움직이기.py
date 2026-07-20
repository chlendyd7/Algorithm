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

from collections import deque
from itertools import product


direction = [(0,1), (1,0), (-1,0), (0,-1)]
def solution(maze):
    n, m = len(maze), len(maze[0])
    for i in range(n):
        for j in range(m):
            if maze[i][j] == 1: r = (i,j)
            elif maze[i][j] == 2: b = (i,j)
            elif maze[i][j] == 3: r_e = (i,j)
            elif maze[i][j] == 4: b_e = (i,j)
    
    r_visited = [[0] * m for _ in range(n)]
    b_visited = [[0] * m for _ in range(n)]
    r_visited[r[0]][r[1]] = True
    b_visited[b[0]][b[1]] = True

    answer = 1e9
    
    def dfs(r, b, cnt):
        nonlocal answer
        if cnt >= answer:
            return
        
        if r == r_e and b == b_e:
            answer = min(answer, cnt)
            return

        r_lst = []
        if r == r_e:
            r_lst.append(r)
        else:
            for dx, dy in direction:
                nx, ny = r[0] + dx, r[1] + dy
                if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] != 5:
                    if not r_visited[nx][ny]:
                        r_lst.append((nx,ny))

        b_lst = []
        if b == b_e:
            b_lst.append(b)
        else:
            for dx, dy in direction:
                nx, ny = b[0] + dx, b[1] + dy
                if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] != 5:
                    if not b_visited[nx][ny]:
                        b_lst.append((nx,ny))
        
        for rr, bb in product(r_lst, b_lst):
            if rr == bb: continue
            if rr == b and bb == r: continue
            r_visited[rr[0]][rr[1]] = True
            b_visited[bb[0]][bb[1]] = True
            dfs(rr, bb, cnt+1)
            r_visited[rr[0]][rr[1]] = False
            b_visited[bb[0]][bb[1]] = False

        
    dfs(r,b,0)
    return answer if answer != 1e9 else 0

print(solution([[1, 4], [0, 0], [2, 3]])) # 3
print(solution([[1, 0, 2], [0, 0, 0], [5, 0 ,5], [4, 0, 3]])) # 7
