n = int(input())
stack = []
answer = 0

for i in range(n):
    h = int(input())
    cnt = 1

    while stack and stack[-1][0] <= h:
        top = stack[-1]
        answer += top[1]
        if top[0] == h:
            cnt += top[1]
        stack.pop()

    if stack:
        answer += 1
    
    stack.append((h,cnt))

print(answer)