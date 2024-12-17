import sys

# 파일을 합치는데 필요한 최소 비용을 계산하는 함수
def min_merge_cost(files):
    n = len(files)
    dp = [[0] * n for _ in range(n)]  # dp[i][j]: i부터 j까지 파일을 합치는데 필요한 최소 비용

    # 파일의 부분합 미리 계산
    prefix_sum = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix_sum[i] = prefix_sum[i - 1] + files[i - 1]

    # 대각선 길이 1부터 n-1까지 순회
    for length in range(1, n):
        for i in range(n - length):
            j = i + length
            dp[i][j] = float('inf')  # 무한대로 초기화

            # 파일을 합치는 모든 경우의 수를 고려하여 최소 비용 계산
            for k in range(i, j):
                cost = dp[i][k] + dp[k + 1][j] + prefix_sum[j + 1] - prefix_sum[i]
                dp[i][j] = min(dp[i][j], cost)

    return dp[0][n - 1]

# 테스트 케이스 수 입력
t = int(input().strip())

# 각 테스트 케이스에 대해
for _ in range(t):
    # 장의 수 입력
    k = int(input().strip())
    # 파일 크기 입력
    files = list(map(int, input().split()))


prefix_sum = [0, 40, 70, 100, 150]

    # 최소 비용 계산하여 출력
dp[0][1] = min(dp[0][0] + dp[1][1] + (prefix_sum[2] - prefix_sum[0])) = 70
dp[1][2] = min(dp[1][1] + dp[2][2] + (prefix_sum[3] - prefix_sum[1])) = 60
dp[2][3] = min(dp[2][2] + dp[3][3] + (prefix_sum[4] - prefix_sum[2])) = 80

dp[0][2] = min(dp[0][0] + dp[1][2] + (prefix_sum[3] - prefix_sum[0]), dp[0][1] + dp[2][2] + (prefix_sum[3] - prefix_sum[0])) = 170
dp[1][3] = min(dp[1][1] + dp[2][3] + (prefix_sum[4] - prefix_sum[1]), dp[1][2] + dp[3][3] + (prefix_sum[4] - prefix_sum[1])) = 160

dp[0][3] = min(dp[0][0] + dp[1][3] + (prefix_sum[4] - prefix_sum[0]), dp[0][1] + dp[2][3] + (prefix_sum[4] - prefix_sum[0]), dp[0][2] + dp[3][3] + (prefix_sum[4] - prefix_sum[0])) = 300

cost = dp[i][k] + dp[k+1][j] + prefix_sum[j +1] - prefix_sum[i]
