n, d = map(int,input().split())
answer = 0
high_ways = []
for _ in range(n):
    start, end, length = map(int,input().split())
    if end - start > length:
        high_ways.append((start, end, length))
high_ways.sort()
dp = [i for i in range(d+1)]

for start, end, length in high_ways:
    for i in range(1, d+1):
        if end == i:
            dp[i] = min(dp[i], dp[start] + length)
        else:
            dp[i] = min(dp[i], dp[i-1]+1)

print(dp[d])
