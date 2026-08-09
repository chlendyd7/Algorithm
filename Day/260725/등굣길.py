# https://school.programmers.co.kr/learn/courses/30/lessons/42898
def solution(m, n, puddles):
    dp = [[0] * (m+1) for _ in range(n+1)]
    dp[1][1] = 1

    for c in range(1, n+1):
        for r in range(1, m+1):
            if c == 1 and r == 1:
                continue
            if [r,c] in puddles:
                continue
            dp[c][r] = dp[c][r-1] + dp[c-1][r]

    return dp[n][m] % 1000000007

