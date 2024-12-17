import sys
input = sys.stdin.readline

t = int(input())

def min_merge_cost(files):
    
    n = len(files)
    prefix_sum = [0] * (n + 1)

    for i in range(1, n + 1):
        prefix_sum[i] = prefix_sum[i - 1] + files[i - 1]
            
    dp = [[0] * n for _ in range(n)]
    for length in range(1, n):
        for i in range(n-length):
            j = i + length
            dp[i][j] = float('inf')
            for k in range(i,j):
                cost = dp[i][k] + dp[k+1][j] + prefix_sum[j + 1] - prefix_sum[i]
                dp[i][j] = min(cost, dp[i][j])

    print(dp[0][n-1])

for _ in range(t):
    k = int(input())
    files = list(map(int, input().split()))
    min_merge_cost(files)
