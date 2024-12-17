import sys
import math
input = sys.stdin.readline
n = int(input())

rest = list(map(int, input().split())) # 남은 기간
plan = list(map(int, input().split())) # 계획일

arr = []
for r, p in zip(rest, plan): # 기간과 계획을 묶음
    arr.append([r, p])
arr = sorted(arr, key=lambda x: (x[1], x[0]))
p = arr[0][0]
th = arr[0][1]
cnt = 0

for i in range(n):
    if th > arr[i][0]:
        tmp = math.ceil((th - arr[i][0]) / 30)
        cnt += tmp
        arr[i][0] += tmp * 30
    
    p = max(p, arr[i][0])

    if i + 1 < n and arr[i][1] != arr[i+1][1]:
        th = max(p, arr[i+1][1])
print(cnt)
