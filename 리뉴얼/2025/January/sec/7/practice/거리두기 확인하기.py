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
            x, y = q.popleft()
            
            direction = [(1,0), (-1,0), (0,1), (0,-1)]
            
            for i in range(4):
                nx = x + direction[i][0]
                ny = y + direction[i][1]
                
                if 0<= nx < 5 and 0<= ny < 5 and visited[nx][ny] == 0:
                    if place[nx][ny] == 'O':
                        q.append([nx,ny])
                        visited[nx][ny] = 1
                        distance[nx][ny] = distance[x][y] + 1

                    if place[nx][ny] == 'P' and distance[x][y] <= 1:
                        return 0
    return 1

def solution(places):
    answer = []


    for p in places:
        answer.append(bfs(p))
    return answer