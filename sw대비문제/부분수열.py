def dfs(level, sum_sub):
    global cnt
    if level >= N:
        return
    if sum_sub + arr[level] == S:
        cnt += 1
    dfs(level + 1, sum_sub + arr[level]) #level번째 원소를 부분수열에 포함
    dfs(level + 1, sum_sub)              #level번쨰 원소를 부분수열에 미포함


N, S = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0
dfs(0, 0)
print(cnt)
# [출처] ⚪[Python, 파이썬] 백준 1182번 : 부분수열의 합|작성자 Dohyeong Kim

