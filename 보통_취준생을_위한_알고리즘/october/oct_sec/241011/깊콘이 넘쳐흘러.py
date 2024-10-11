import math


n = int(input())
emoticon = list(map(int ,input().split()))
plan = list(map(int, input().split()))

arr = []
for e, p in zip(emoticon, plan):
    arr.append([e, p])

arr.sort(key=lambda x: (x[1], x[0]))
now = arr[0][0]
now_plan = arr[0][1]
cnt = 0
for i in range(n):
    if now_plan > arr[i][0]:
        tmp = math.ceil((now_plan - arr[i][0]) / 30)
        cnt += tmp
        arr[i][0] += (30 * tmp)
    now = max(now, arr[i][0])

    if i+1 < n and arr[i][1] != arr[i+1][1]:
        now_plan = max(now_plan, arr[i+1][1])
print(cnt) 