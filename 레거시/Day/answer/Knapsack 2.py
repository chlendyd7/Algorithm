n, W = map(int, input().split())
bags = [list(map(int, input().split())) for _ in range(n)]

max_value = sum(v for w,v in bags)

INF = 10**18
dp = [INF] * (max_value+1)
dp[0] = 0

for w, v in bags:
    for i in range(max_value, v-1, -1):
        if dp[i-v] != INF:
            dp[i] = min(dp[i], dp[i-v] + w)

for i in range(max_value, 0, -1):
    if dp[i] <= W:
        print(i)
        break
