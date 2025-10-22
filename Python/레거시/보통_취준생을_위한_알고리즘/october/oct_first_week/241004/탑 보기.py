n = int(input())
buildings = list(map(int, input().split()))

left_result = [(0,-1)] * n
right_result = [(0, -1)] * n

stack = []
for i in range(n):
    while stack and buildings[stack[-1]] <= buildings[i]:
        stack.pop()
    if stack:
        left_result[i] = (len(stack), stack[-1] + 1)
    else:
        left_result[i] = (0, -1)
    stack.append(i)

stack = []
for i in range(n-1, -1, -1):
    while stack and buildings[stack[-1]] <= buildings[i]:
        stack.pop()
    if stack:
        right_result[i] = (len(stack), stack[-1] + 1)
    else:
        right_result[i] = (0, -1)
    stack.append(i)

for i in range(n):
    visiable_count = left_result[i][0] + right_result[i][0]
    closet = []

    if left_result[i][1] != -1:
        closet.append(left_result[i][1])
    if right_result[i][1] != -1:
        closet.append(right_result[i][1])
    
    if visiable_count == 0:
        print(0)
    else:
        print(visiable_count, min(closet, key=lambda x: abs(x - (i+1))))
