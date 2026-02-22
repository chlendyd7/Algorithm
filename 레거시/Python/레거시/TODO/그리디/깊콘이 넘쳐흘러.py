import sys
import math
input = sys.stdin.readline
n = int(input())  # 입력받을 작업의 개수

remaining_days = list(map(int, input().split()))  # 각 작업의 남은 기간
planned_days = list(map(int, input().split()))  # 각 작업의 계획된 날짜

tasks = []
for remaining, planned in zip(remaining_days, planned_days):  # 남은 기간과 계획된 날짜를 묶어서 리스트에 저장
    tasks.append([remaining, planned])

# 계획된 날짜를 기준으로 오름차순, 남은 기간을 두 번째 기준으로 정렬
tasks = sorted(tasks, key=lambda x: (x[1], x[0]))

current_remaining = tasks[0][0]  # 첫 번째 작업의 남은 기간
current_plan = tasks[0][1]  # 첫 번째 작업의 계획된 날짜
total_adjustments = 0  # 총 조정 횟수

for i in range(n):
    if current_plan > tasks[i][0]:
        required_adjustments = math.ceil((current_plan - tasks[i][0]) / 30)  # 조정할 횟수 계산
        total_adjustments += required_adjustments
        tasks[i][0] += required_adjustments * 30  # 남은 기간을 조정된 값으로 업데이트

    current_remaining = max(current_remaining, tasks[i][0])  # 가장 긴 남은 기간 갱신

    # 다음 작업과 계획된 날짜가 다를 경우, 다음 작업의 계획된 날짜와 남은 기간 비교
    if i + 1 < n and tasks[i][1] != tasks[i+1][1]:
        current_plan = max(current_remaining, tasks[i+1][1])

print(total_adjustments)
