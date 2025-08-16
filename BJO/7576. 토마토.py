from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

M, N = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]

q = deque()
zero_count = 0
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            visited[i][j] = 1
            q.append((i, j))
        elif graph[i][j] == 0:
            zero_count += 1

# 첫 번째 큐에 들어가있는 지점은 0일차이므로
days = -1
while q:
    size_q = len(q)
    # step 증가(시작점으로부터의 거리인 셈)
    # 0일차부터 시작
    days += 1
    # 이전 일자에서 추가된 만큼만 큐에서 비워내기
    for _ in range(size_q):
        r, c = q.popleft()

        for dir in range(4):
            nr = r + dr[dir]
            nc = c + dc[dir]
            
            if nr < 0 or nr >= N or nc < 0 or nc >= M:
                continue
            
            if graph[nr][nc] == 0 and not visited[nr][nc]:
                visited[nr][nc] = 1
                q.append((nr, nc))
                zero_count -= 1

if zero_count == 0:
    print(days)
else:
    print(-1)
