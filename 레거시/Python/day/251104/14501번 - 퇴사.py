import sys
input = sys.stdin.readline

N = int(input())
T, P = [], []
for _ in range(N):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)

dp = [0] * (N+2)

for i in range(N, 0, -1):
    if i + T[i-1] > N+1:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1], P[i-1] + dp[i + T[i-1]])

print(dp[1])
