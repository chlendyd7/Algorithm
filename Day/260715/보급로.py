# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV15QRX6APsCFAYD
'''
    결과 값들을 다 저장하면서
    최종적으로 N,N 좌표에 있는게 가장 작지 않을까
'''
import heapq


def simulation():
    N = int(input())
    board = [list(map(int, input())) for _ in range(N)]
    value = [[1e9] * N for _ in range(N)]
    hq = [(0,0,0)]
    value[0][0] = 0
    while hq:
        now_v, now_x, now_y = heapq.heappop(hq)
        if value[now_x][now_y] < now_v:
            continue

        for dx, dy in [(1,0),(0,1),(-1,0),(0,-1)]:
            nx, ny = now_x+dx, now_y+dy
            if 0 <= nx < N and 0 <= ny < N:
                next_v = now_v + board[nx][ny]
                if value[nx][ny] > next_v:
                    value[nx][ny] = next_v
                    heapq.heappush(hq, (next_v, nx, ny))

    return value[N-1][N-1]

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    print(f'#{test_case} {simulation()}')
