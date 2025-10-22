def dfs(idx, sum):
    global answer
    if idx >= n:
        return

    sum += lst[idx]
    if s==sum:
        answer += 1

    dfs(idx+1, sum-lst[idx])
    dfs(idx+1, sum)

n,s = map(int,input().split())
lst = list(map(int,input().split()))
answer = 0
dfs(0, 0)
print(answer)
