def osu(ls):
    count = len(ls)
    result = [-1] * count
    stack = []
    for idx in range(count):
        while stack and ls[stack[-1]] < ls[idx]:
            stack_idx = stack.pop()
            result[stack_idx] = ls[idx]
        stack.append(idx)

    return result

n = int(input())
ls = list(map(int,input().split()))

print(' '.join(map(str, osu(ls))))
