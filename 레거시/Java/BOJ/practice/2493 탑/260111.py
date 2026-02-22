n = int(input())
tops = list(map(int, input().split()))

stack = []
result = [0] * n
for i in range(n):
    # if not stack:
    #     stack.append((i+1, tops[i]))
    #     continue

    while stack:
        if stack[-1][1] >= tops[i]:
            result[i] = stack[-1][0]
            break
        else:
            stack.pop()

    stack.append((i+1, tops[i]))

print(*result)
