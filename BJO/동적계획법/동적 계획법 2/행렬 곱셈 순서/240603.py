import sys
input = sys.stdin.readline

# 행렬의 개수
n = int(input().strip())

# 행렬의 크기 리스트
matrices = []
for _ in range(n):
    r, c = map(int, input().split())
    matrices.append((r, c))

# dp[i][j]는 i번째 행렬부터 j번째 행렬까지 곱하는데 필요한 최소 연산 횟수
dp = [[0] * n for _ in range(n)]

# 대각선 길이 1부터 n-1까지
for length in range(1, n):
    for i in range(n - length):
        j = i + length
        dp[i][j] = float('inf')
        # 행렬 곱셈 순서를 k로 나누어 계산
        for k in range(i, j):
            cost = dp[i][k] + dp[k + 1][j] + matrices[i][0] * matrices[k][1] * matrices[j][1]
            if cost < dp[i][j]:
                dp[i][j] = cost

# 0번째 행렬부터 n-1번째 행렬까지 곱하는데 필요한 최소 연산 횟수
print(dp[0][n - 1])
