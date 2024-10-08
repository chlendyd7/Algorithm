from collections import deque


dx = [1,0,-1,0]
dy = [0,1,0,-1]
first_dx = [1,-1]

def solution(map, point):
    n = len(map)
    visit = [[0]*n for _ in range(n)]
    q = deque()
    x,y = point[0], point[1]
    visit[x][y] = 1
    q.append([x,y,0])
    
    while q:
        x,y,cnt = q.popleft()
        
        if map[x][y] == 7:
            return True

        if cnt == 0:
            for k in range(2):
                nx = x + first_dx[k]
                if 0<= nx <n and 0<= y < n and not visit[nx][y]:
                    visit[nx][y] = 1
                    q.append([nx,y,1])
        else:
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if 0<= nx < n and 0<= ny < n and not visit[nx][ny]:
                    if map[nx][ny] not in [0,8]:
                        visit[nx][ny] = 1
                        q.append([nx,ny,1])
    return False