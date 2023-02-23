def dfs(level, sum_sub):
    global cnt
    if level >= N:
        return
    if sum_sub + arr[level] == S:
        cnt +=1
    dfs(level +1, sum_sub + arr[level])
    dfs(level +1, sum_sub)





N, S = map(int,input().split())
arr = list(map(int,input().split()))
cnt = 0
dfs(0,0)
print(cnt)