N, M = map(int, input().split())
bytes = list(map(int, input().split()))
costs = list(map(int, input().split()))
max_cost = sum(costs)
dp = [0] * (max_cost + 1)
for i in range(N):
    curr_m = bytes[i]
    curr_c = costs[i]
    for j in range(max_cost, curr_c - 1, -1):
        dp[j] = max(dp[j], dp[j-curr_c] + curr_m)

for c in range(max_cost + 1):
    if dp[c] >= M:
        print(c)
        break
