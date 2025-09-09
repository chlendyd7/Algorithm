N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
print(arr)
arr.sort(key=lambda x:x[1])
dp = [0] * (K+1)
for w, v in arr:
    dp[w] = max(dp[w], v)
for i in range(0, K+1):
    dp
print(arr)