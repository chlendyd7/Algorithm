def solution(m, n, puddles):
    # DP 배열 초기화
    dp = [[0] * n for _ in range(m)]
    
    # 장애물 위치 설정
    for x, y in puddles:
        dp[x - 1][y - 1] = -1  # 장애물 위치에 -1 표시

    dp[0][0] = 1  # 시작점 초기화

    for i in range(m):
        for j in range(n):
            if dp[i][j] == -1:  # 장애물이 있는 경우
                continue
            if i > 0 and dp[i-1][j] != -1:  # 위쪽에서 오는 경로
                dp[i][j] += dp[i-1][j]
            if j > 0 and dp[i][j-1] != -1:  # 왼쪽에서 오는 경로
                dp[i][j] += dp[i][j-1]

            dp[i][j] %= 1000000007  # 1,000,000,007로 나눈 나머지

    return dp[m-1][n-1]  # 도착점의 경로 수 반환

# 예시 실행
m = 4
n = 3
puddles = [[2, 2]]
print(solution(m, n, puddles))  # 출력: 4
