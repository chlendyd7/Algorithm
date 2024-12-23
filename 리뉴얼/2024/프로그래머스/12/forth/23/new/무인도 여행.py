from collections import deque

direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
def bfs(h, w, i, j):
    global visited
    cnt = 0
    q = deque()
    q.append([i,j])
    while q:
        x,y = q.popleft()
        for k in range(4):
            dx = x + direction[k][0]
            dy = y + direction[k][1]
            if 0<= dx < h and 0<= dy < w:
                if not visited[nx][ny] and maps[dx][dy] != 'X':
                    cnt += maps[dx][dy]
                    q.append([dx,dy])
    return cnt
    
def solution(maps):
    h, w = len(maps), len(maps[0])
    visited = [[False] * len(maps) for _ in range(len(maps))]
    answer = []
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] != 'X' and not visited[i][j]:
                answer.append(bfs(h, w, i,j))
            
    if answer:
        return answer.sort()
    else:
        return [-1]
