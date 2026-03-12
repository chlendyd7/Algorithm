import sys

INT_MAX = sys.maxsize
MAX_N = 100
MAX_K = 100
DIR_NUM = 4


# 격자 안에 들어오는지 확인합니다.
def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


def find_min(i, j, l):
    # 이미 계산해본 적이 있다면 바로 반환합니다.
    if dp[i][j][l] != -1:
        return dp[i][j][l]

    # l이 1이라면 더 이상 진행할 필요가 없기 때문에
    # dp값은 0이 됩니다.
    if l == 1:
        dp[i][j][l] = 0
        return dp[i][j][l]

    # 인접한 4방향을 살펴봅니다.
    best = INT_MAX
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for t in range(4):
        nx, ny = i + dx[t], j + dy[t]
        if in_range(nx, ny) and grid[nx][ny] > grid[i][j]:
            best = min(best, max(find_min(nx, ny, l - 1), grid[nx][ny] - grid[i][j]))

    dp[i][j][l] = best
    return dp[i][j][l]


# 변수 선언 및 입력
n, k = tuple(map(int, input().split()))
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

# dp값을 전부 -1로 초기화해줍니다.
dp = [
    [
        [-1] * (MAX_K + 1) 
        for _ in range(MAX_N)
    ] 
    for _ in range(MAX_N)
]

# 각 위치를 시작으로 하는 dp를 진행합니다.
ans = INT_MAX
for i in range(n):
    for j in range(n):
        ans = min(ans, find_min(i, j, k))

# 여전히 INT_MAX라면
# 불가능하다는 뜻이므로 답은 -1이 됩니다.
if ans == INT_MAX:
    ans = -1

print(ans)
