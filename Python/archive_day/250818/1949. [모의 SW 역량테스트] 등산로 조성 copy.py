# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PoOKKAPIDFAUq

DIRECTION = [(1,0), (-1,0), (0,1), (0,-1)]

def solution():
    N, K = map(int, input().split())
    mountain = [list(map(int, input().split())) for _ in range(N)]

    # 가장 높은 봉우리 찾기
    mx = max(max(row) for row in mountain)
    start_points = [(i, j) for i in range(N) for j in range(N) if mountain[i][j] == mx]

    result = 0

    def dfs(r, c, distance):
        nonlocal result
        result = max(result, distance)
        for dx, dy in DIRECTION:
            nx, ny = r + dx, c + dy
            if 0 <= nx < N and 0 <= ny < N and mountain[nx][ny] < mountain[r][c]:
                dfs(nx, ny, distance + 1)

    # 모든 칸을 최대 K 깊이만큼 깎아보기
    for i in range(N):
        for j in range(N):
            original = mountain[i][j]
            for k in range(0, K+1):  # 0일 때는 안 깎는 경우
                mountain[i][j] = original - k
                for sr, sc in start_points:
                    dfs(sr, sc, 1)
            mountain[i][j] = original  # 원상 복구

    return result


T = int(input())
for t in range(1, T+1):
    print(f'#{t} {solution()}')
