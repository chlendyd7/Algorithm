def solution(triangle):
    n = len(triangle)
    dp = [[0] * (i + 1) for i in range(n)]  # dp 배열 크기 조정
    dp[0][0] = triangle[0][0]  # 첫 번째 요소 초기화

    for i in range(1, n):
        for j in range(i + 1):
            if j == 0:  # 첫 번째 요소인 경우
                dp[i][j] = dp[i - 1][j] + triangle[i][j]
            elif j == i:  # 마지막 요소인 경우
                dp[i][j] = dp[i - 1][j - 1] + triangle[i][j]
            else:  # 중간 요소인 경우
                dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j]) + triangle[i][j]

    return max(dp[-1])  # 마지막 행에서 최대 값 반환

# 예시 실행
triangle = [
    [2],
    [3, 4],
    [6, 5, 7],
    [4, 1, 8, 3]
]
print(solution(triangle))  # 출력: 18
