

# import os
# import sys
import heapq


# BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # 현재 실행 중인 파일의 절대 경로
# sys.stdin = open(os.path.join(BASE_DIR, 'input.txt'), 'r')


dirs = [(-1,0), (1,0), (0,1), (0,-1)]

def dijkstra(N, board):
    INF = 1e9
    dist = [[INF] * N for _ in range(N)]
    dist[0][0] = board[0][0]
    pq = [(board[0][0], 0, 0)]

    while pq:
        cost, x, y = heapq.heappop(pq)

        if dist[x][y] < cost:
            continue

        if x == N-1 and y == N-1:
            return cost

        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if 0<= nx < N and 0<= ny < N:
                ncost = cost+board[nx][ny]
                if ncost < dist[nx][ny]:
                    dist[nx][ny] = ncost
                    heapq.heappush(pq, (ncost, nx, ny))

    return dist[N-1][N-1]

def solution():
    N = int(input())
    board = [list(map(int, input())) for _ in range(N)]
    num = dijkstra(N, board)
    return num


T = int(input())
for t in range(1, T+1):
    print(f'#{t} {solution()}')
