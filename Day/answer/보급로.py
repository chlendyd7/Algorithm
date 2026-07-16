# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV15QRX6APsCFAYD
'''
    결과 값들을 다 저장하면서
    최종적으로 N,N 좌표에 있는게 가장 작지 않을까
'''
import heapq


def simulation():
    n = int(input())
    board = [list(map(int, input())) for _ in range(n)]
    visited = [[10**18] * n for _ in range(n)]
    visited[0][0] = 0
    hq = [(0, 0, 0)]
    while hq:
        w, x, y = heapq.heappop(hq)
        if visited[x][y] < w:
            continue

        for dx, dy in [(0,1), (1,0), (-1,0), (0,-1)]:
            nx, ny = x + dx, y + dy
            if 0<= nx < n and 0 <= ny < n:
                nxt = w + board[nx][ny]
                if visited[nx][ny] > nxt:
                    visited[nx][ny] = nxt
                    heapq.heappush(hq, (nxt, nx, ny))

    return visited[n-1][n-1]

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    print(f'#{test_case} {simulation()}')
