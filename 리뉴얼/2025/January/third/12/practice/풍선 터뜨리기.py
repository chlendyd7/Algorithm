def solution(a):
    answer = 2
    N = len(a)
    dp = [[0] * N for _ in range(2)]
    dp[0][0] = a[0]
    dp[1][-1] = a[-1]
    
    for i in range(1, N):
        dp[0][i] = min(dp[0][i-1], a[i])
    for i in range(N - 2, -1, -1):
        dp[1][i] = min(dp[1][i+1], a[i])
    
    for i in range(1, N-1):
        left_min = dp[0][i-1]
        right_min = dp[1][i+1]
    
    for i in range(N):
        if a[i] <= left_min[i] or a[i] <= right_min[i]:
            answer += 1
    return answer
solution([9,-1,-5])