n = int(input())
towers = list(map(int, input().split()))

stack = []
ans = [0] * n
for i in range(n):
    while stack and stack[-1][1] > towers[i]:
        ans[i] = stack[-1][0] + 1
        break
    else:
        stack.pop()
    stack.append((i,towers[i]))

print(*ans)