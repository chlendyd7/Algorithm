import math


n = int(input())
gift_con = list(map(int, input().split()))
plan = list(map(int, input().split()))

arr = []
for g, p in zip(gift_con, plan):
    arr.append([g, p])
arr.sort(key=lambda x: x[1])

now_use = arr[0][0]
now_plan = arr[0][1]
cnt = 0
for i in range(n):
    if now_plan > now_use:
        tmp = math.ceil((now_plan - arr[i][0]) / 30)
        cnt += tmp
        arr[i][0] += tmp * 30
    
    now_plan = max(now_use, arr[i][0])

    if i+1 < n and arr[i][1] != arr[i+1][1]:
        now_plan = max(now_plan, arr[i+1][1])
print(cnt)
