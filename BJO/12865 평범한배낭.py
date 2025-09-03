N, K = map(int, input().split())
bags = [list(map(int, input().split())) for _ in range(N)]
bags.sort(key=lambda x: x[0])
dp = [0] * (K+1)
for i in range(1, N+1):
    w, v = bags[i-1]
    for j in range(K, w-1, -1):
        dp[j] = max(dp[j], dp[j-w] + w)

print(dp[K])
