n = int(input())
towers = list(map(int,input().split()))
answer_lst = [0] * n
stack = []
for i in range(n):
    while stack:
        if stack[-1][1] > towers[i]:
            answer_lst[i] = stack[-1][0] + 1
            break
        else:
            stack.pop()

    stack.append((i, towers[i]))
print(*answer_lst)