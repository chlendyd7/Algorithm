# 풀이 1: 백트래킹

def dfs(n, sm):
    global ans
    # [1] 종료조건: 가능한 n을 종료에 관련된것으로 정의!
    if n>=N:
        ans = max(ans, sm)
        return

    # [2] 하부호출: 화살표 개수만큼 호출
    if n+T[n]<=N:   # 상담하는 경우(퇴사일전 완료 가능할 때만 상답)
        dfs(n+T[n], sm+P[n])
    dfs(n+1, sm)    # 상담 하지 않는 경우(항상 가능)

N = int(input())
T = [0]*N
P = [0]*N
for i in range(N):
    T[i], P[i] = map(int, input().split())

ans = 0
dfs(0, 0)
print(ans)

# 풀이 2: DP

N = int(input())
T = [0]*N
P = [0]*N
for i in range(N):
    T[i], P[i] = map(int, input().split())

dp = [0]*(N+1)
for n in range(N-1, -1, -1):    # 뒤에서 앞으로(완료기준)
    if n+T[n]<=N:               # 기간내 상담완료 가능
        dp[n]=max(dp[n+1], dp[n+T[n]]+P[n])
    else:
        dp[n]=dp[n+1]

print(dp[0])