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
    def make_node(node, node_end, visited):
        nxt = []
        if node == node_end:
            nxt = [node_end]
        else:
            for dx, dy in direction:
                nx, ny = node[0] + dx, node[1] + dy
                if 0 <= nx < n and 0 <= ny < m:
                    if not visited[nx][ny] and maze[nx][ny] != 5:
                        nxt.append((nx,ny))
        return nxt

    n, m = len(maze), len(maze[0])
    for i in range(n):
        for j in range(m):
            if maze[i][j] == 1: r = (i,j)
            if maze[i][j] == 2: b = (i,j)
            if maze[i][j] == 3: r_end = (i,j)
            if maze[i][j] == 4: b_end = (i,j)


    q = deque()
    r_visitied = [[False] * m for _ in range(n)]
    b_visitied = [[False] * m for _ in range(n)]
    q.append((r,b,0))
    r_visitied[r[0]][r[1]] = True
    b_visitied[b[0]][b[1]] = True
    
    
    while q:
        r, b, w = q.popleft()
        if r == r_end and b == b_end:
            return w
        else:
            r_lst = make_node(r, r_end, r_visitied)
            b_lst = make_node(b, b_end, b_visitied)
            
        for nxt_r, nxt_b in product(r_lst, b_lst):
            if nxt_r == b and nxt_b == r: continue
            if nxt_r == nxt_b: continue

            q.append((nxt_r, nxt_b, w + 1))




    return -1

print(solution([[1, 4], [0, 0], [2, 3]])) # 3
print(solution([[1, 0, 2], [0, 0, 0], [5, 0 ,5], [4, 0, 3]])) # 7
