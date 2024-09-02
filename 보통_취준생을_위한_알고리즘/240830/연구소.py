'''
    바이러스에 벽을 세우기
    바이러스 퍼뜨리기
    0 갯수 세기
'''

from collections import deque

def bfs():
    global answer

    for x in range(N):
        for y in range(M):
            visit[x][y] = lab[x][y]
            if lab[x][y] == 2:
                q.append([x,y])

    while q:
        x,y = q.popleft()
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if 0<= xx < N and 0<= yy < M and lab[xx][yy] == 0 and visit[xx][yy] == 0:
                q.append([xx, yy])
                visit[xx][yy] = 1

    cnt = 0
    for x in range(N):
        for y in range(M):
            if lab[x][y] == 0 and visit[x][y] == 0:
                cnt +=1
    answer = max(answer, cnt)

def back_traking(selct):
    if selct == 3:
        bfs()
        return
    for x in range(N):
        for y in range(M):
            if lab[x][y] == 0 and visit2[x][y] == 0:
                visit2[x][y] = 1
                lab[x][y] = 1
                back_traking(selct + 1)
                lab[x][y] = 0
                visit2[x][y] = 0



N, M = map(int,input().split())
lab = [list(map(int,input().split())) for _ in range(N)]

visit = [[0 for _ in range(M)] for _ in range(N)]
visit2 = [[0 for _ in range(M)] for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

q = deque()
answer = 0
back_traking(0)
print(answer)