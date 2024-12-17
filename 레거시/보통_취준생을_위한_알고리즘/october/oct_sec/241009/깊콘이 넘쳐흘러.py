import sys
import math
input = sys.stdin.readline
n = int(input())  # 입력받을 작업의 개수

remaining_days = list(map(int, input().split()))  # 각 작업의 남은 기간
planned_days = list(map(int, input().split()))  # 각 작업의 계획된 날짜

tasks = []
for remaining, planned in zip(remaining_days, planned_days):  # 남은 기간과 계획된 날짜를 묶어서 리스트에 저장
    tasks.append([remaining, planned])

tasks.sort(key=lambda x: (x[1], x[0]))

remain = tasks[0][0]
plan = tasks[0][1]
cnt = 0
for i in range(n):
    if plan > tasks[i][0]:
        tmp = math.ceil((plan - tasks[i][0]) / 30)
        cnt += tmp
        tasks[i][0] += tmp * 30
    
    remain = max(remain, tasks[i][0])

    if i + 1 < n and tasks[i][1] != tasks[i+1][1]:
        plan = max(remain, tasks[i+1][1])

print(cnt)