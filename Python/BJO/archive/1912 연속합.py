# import sys
# sys.stdin = open('input.txt', 'r')
N = int(input())
nums = list(map(int, input().split()))
dp = [-1e9] * (N+1)
dp[0] = nums[0]
for i in range(1, N):
    for j in range(i, N):
        dp[j] = max(nums[j], dp[j-1] + nums[j])

print(max(dp))

n = int(input())
arr = list(map(int, input().split()))

dp = [0] * n
dp[0] = arr[0]

for i in range(1, n):
    dp[i] = max(arr[i], dp[i-1] + arr[i])

print(max(dp))