n = int(input())
papers = []
for _ in range(n):
    nums = sorted(map(int, input().split()))
    papers.append((nums[1], nums[0]))

# 긴 게 으로
papers.sort(key=lambda x:(-x[0] -x[1]))
dp = [0] * n
for i in range(n):
    for j in range(i+1, n):
        if papers[i][1] >= papers[j][1]:
            dp[j] = dp[j] + 1

print(max(dp))
