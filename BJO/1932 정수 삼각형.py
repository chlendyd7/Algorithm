N = int(input())
dp = [[0] * (N+1) for _ in range(N)]
nums = []
for _ in range(N):
    nums.append(list(map(int, input().split())))

dp[0][0] = nums[0][0]
for i in range(1, N):
    for j in range(0, i+1):
        if j==0: #왼쪽
            dp[i][j] = dp[i-1][0] + nums[i][j]
        if j==i: #오른쪽
            dp[i][j] = dp[i-1][j-1] + nums[i][j]
        else:
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + nums[i][j]

print(max(dp[N-1]))
