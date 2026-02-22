n = int(input())  # 탑의 수
heights = list(map(int, input().split()))  # 탑의 높이

# 결과를 저장할 리스트
left_result = [(0, -1)] * n  # (보이는 탑 수, 가장 가까운 탑 번호)
right_result = [(0, -1)] * n  # (보이는 탑 수, 가장 가까운 탑 번호)

# 스택을 이용해 왼쪽을 보는 경우 처리
stack = []
for i in range(n):
    while stack and heights[stack[-1]] <= heights[i]:
        stack.pop()
    if stack:
        left_result[i] = (len(stack), stack[-1] + 1)
    else:
        left_result[i] = (0, -1)
    stack.append(i)

# 스택을 이용해 오른쪽을 보는 경우 처리
stack = []
for i in range(n - 1, -1, -1):
    while stack and heights[stack[-1]] <= heights[i]:
        stack.pop()
    if stack:
        right_result[i] = (len(stack), stack[-1] + 1)
    else:
        right_result[i] = (0, -1)
    stack.append(i)

# 결과 출력
for i in range(n):
    visible_count = left_result[i][0] + right_result[i][0]
    closest = []

    if left_result[i][1] != -1:
        closest.append(left_result[i][1])
    if right_result[i][1] != -1:
        closest.append(right_result[i][1])

    if visible_count == 0:
        print(0)
    else:
        print(visible_count, min(closest, key=lambda x: abs(x - (i + 1))))
