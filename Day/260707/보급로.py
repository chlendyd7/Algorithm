# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV15QRX6APsCFAYD
import heapq


def simulation():
    N = int(input())
    board = [list(map(int, input())) for _ in range(N)]
    dist = [[1e9] * N for _ in range(N)]
    pq = []
    dist[0][0] = board[0][0]
    heapq.heappush(pq, (dist[0][0], 0, 0))
    while pq:
        curr_dist, r, c = heapq.heappop(pq)
        if curr_dist > dist[r][c]:
            continue
        
        if r == N-1 and c == N-1:
            return curr_dist

        for dr, dc in [(1,0), (0,1), (-1,0), (0,-1)]:
            nr = r + dr
            nc = c + dc
            if 0 <= nr < N and 0 <= nc < N:
                next_dist = curr_dist + board[nr][nc]
                if next_dist < dist[nr][nc]:
                    dist[nr][nc] = next_dist
                    heapq.heappush(pq, (next_dist, nr, nc))
        
    return -1

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    print(f'#{test_case} {simulation()}')
