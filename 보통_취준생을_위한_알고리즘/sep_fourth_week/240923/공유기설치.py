n,c = map(int,input().split())
lst = [int(input()) for _ in range(n)]
lst.sort()
left, right = 1, lst[-1] - lst[0]
result = 0


while left <= right:
    mid = (left + right) // 2
    now = 0
    cnt = 1
    for i in range(n):
        if lst[i] - lst[now] >= mid:
            now = i
            cnt += 1
    if cnt >= c:
        left = mid + 1
        result = mid
    else:
        right = mid - 1

print(result)
