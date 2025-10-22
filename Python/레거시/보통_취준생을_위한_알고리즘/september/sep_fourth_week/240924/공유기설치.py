n,c = map(int,input().split())
lst = [int(input()) for _ in range(n)]
lst.sort()
lt = 1
rt = lst[-1] - lst[0]
answer = 0

while lt <= rt:
    mid = (lt + rt) // 2
    now = 0
    cnt = 1
    for i in range(n):
        if lst[i] - lst[now] >= mid:
            now = i
            cnt += 1
    if cnt >= c:
        lt = mid + 1
        answer = mid
    else:
        rt = mid - 1

print(answer)
