
n = int(input())
buildings = list(map(int, input().split()))
right = [(0, -1)] * n
left = [(0, -1)] * n

stack = []
for i in range(n):
    while stack and buildings[stack[-1]] <= buildings[i]:
        stack.pop()
    if stack:
        left[i] = (len(stack), stack[-1] + 1)
    else:
        left[i] = (0,-1)
    stack.append(i)

for i in range(n -1, -1, -1):
    
    
    
    now = buildings[i]
