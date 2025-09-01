# https://www.acmicpc.net/problem/16987

# 가지치기
# 최대 값의 경우 남은 횟수로 모두 깨도 (N-n)
# 작거나 같다

def dfs(n, cnt):
    global ans
    if ans >= (cnt+(N-n) * 2):
        return

    if n == N: # 모든 계란을 손에 들고 부딪히기 완료
        ans = max(ans, cnt)
        return
    
    if ans[n][0] <= 0:
        dfs(n+1, cnt)
    else: # 계란 들고있으면서 하나씩 부딪혀보기
        flag = False
        for j in range(N):
            if n == j or arr[j][0] <=0:
                continue
            flag = True
            arr[n][0] -= arr[j][1]
            arr[j][0] -= arr[n][1]
            dfs(n+1, cnt + int(arr[n][0] <= 0) + int(arr[j][0] <= 0))
            arr[n][0] += arr[j][1]
            arr[j][0] += arr[n][1]
        if flag==False:
            dfs(n+1, cnt)

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

ans = 0
# 계란 index, 깨진 계란 개수
dfs(0, 0)
print(ans)