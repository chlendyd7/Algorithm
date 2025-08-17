# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWXRJ8EKe48DFAUo
'''
줄기세포들을 배양 용기에 도포한 후 일정 시간 동안 배양을 시킨 후 줄기 세포의 개수가 몇 개가 되는지 계산하는 시뮬레이션 프로그램을 만들어야 한다.
생명력이라는 수치를 가지고 있음
X의 생명력 수치 -> X시간 지나는 순간 활성화
X시간 동안 살고 그 뒤 죽음 죽은 상태로 해당 그리드 차지
방향에 이미 줄기 세포가 존재하는 경우 해당 방향으로 추가적으로 번식하지 않는다.

동시에 번식하려는 경우 생명력 수치가 높은 줄기 세포가 해당 그리드 셀 차지
세로 크기 N 가로크기 M 50, 50 2500
배양 시간 K 300
크기는 무한
생명력 10 이하

visited를 통해 살아있는지 죽었는지를 담아두기?
dict를 통해서 계속 1에 있는 값들만 뽑아서 돌려주기? dfs?
    dict = {
            1: { # 해당 시간 안에
                2: [(i,j), (i1,i1)], # 레벨을 담아주기
                1: [(i,j), (i3, j3)]
            }
    }
'''

from collections import defaultdict, deque
from pprint import pprint


def solution():
    N, M, K = map(int, input().split())
    row_size = N + 2 * K
    col_size = M + 2 * K
    OFFSET = K
    input_value = [list(map(int, input().split())) for _ in range(N)]
    board = [[0] * col_size for _ in range(row_size)]
    visited = [[0]* col_size for _ in range(row_size)]
    time_dict = defaultdict(lambda: defaultdict(list))
    for i in range(N):
        for j in range(M):
            if input_value[i][j] > 0:
                life = input_value[i][j]
                r, c = i + OFFSET, j + OFFSET
                visited[r][c] = 1
                board[r][c] = life
                time_dict[life][life].append((r,c))

    print(time_dict)
    for t in range(1, K+1):
        for life, cells in sorted(time_dict[t].items(), reverse=True):
            for r, c in cells:
                for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                    nr, nc = r + dr, c + dc
                    if visited[nr][nc] == 0:
                        visited[nr][nc] = 1
                        board[nr][nc] = life
                        time_dict[t + life + 1][life].append((nr, nc))

    cnt = 0
    for i in range(row_size):
        for j in range(col_size):
            if visited[i][j]:
                cnt += 1
    return cnt


T = int(input())
for t in range(1, T+1):
    print(f'#{t} {solution()}')
