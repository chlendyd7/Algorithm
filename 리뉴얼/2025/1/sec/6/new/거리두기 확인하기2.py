from collections import deque


def bfs(place):
    start = []
    
    for i in range(5):
        for j in range(5):
            if place[i][j] == 'P':
                start.append([i,j])
    
    for s in start:
        q = deque([s])
        visited = [[0] * 5 for _ in range(5)]
        distance = [[0] * 5 for _ in range(5)]
        visited[s[0]][s[1]] = 1
        
        while q:
            y, x = q.popleft()
            
            dx = [-1, 1, 0, 0]
            dy = [0, 0, -1, 1]
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if 0<= nx < 5 and 0 <= ny < 5 and visited[ny][nx] == 0:
                    if place[nx][ny] == 'O':
                        q.append([ny, nx])
                        visited[ny][nx] = 1
                        distance[ny][nx]


def solution(places):
    answer = []
    
    for p in places:
        answer.append(bfs(p))
        
    return answer