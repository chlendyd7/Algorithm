# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PoOKKAPIDFAUq
'''
최대한 긴 등산로를 만들 계획
N 8
공사 가능 깊이 5
지형 높이 20
가장 높은 봉우리 5

백트래킹 완탐

N*N board
등산로는 가장 높은 봉우리에서 시작해야함
연결되야함
딱 한 곳을 정해서 최대 K 깊이 만큼 지형을 깎는 공사를 할 수 있다.

모든 곳을 탐색하는게 아닌

bfs가 아닌 dfs로 풀어라고함
'''
DIRECTION = [
    (1,0),
    (-1,0),
    (0,1),
    (0,-1)
]

def solution():
    N, K = map(int, input().split())
    mountain = [list(map(int, input().split())) for _ in range(N)]
    mx = 0
    start_points = []
    mx = max(c for row in mountain for c in row)
    for i in range(N):
        for j in range(N):
            if mountain[i][j] == mx:
                start_points.append((i,j))

    result = 0
    def dfs(r, c, distance):
        nonlocal result
        result = max(result, distance)

        for dx, dy in DIRECTION:
            nx, ny = r + dx, c + dy
            if 0<= nx < N and 0<= ny < N and mountain[nx][ny] < mountain[r][c]:
                dfs(nx, ny, distance + 1)


    for i in range(N):
        for j in range(N):
            for k in range(1, K+1):
                mountain[i][j] -= k
                for sr, sc in start_points:
                    dfs(sr, sc, 1)
                mountain[i][j] += k

    return result
T = int(input())
for t in range(1, T+1):
    print(f'#{t} {solution()}')