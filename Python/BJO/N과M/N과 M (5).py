N,M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

stack = []
def backtracking(depth):
    if depth == M:
        print(' '.join(map(str, stack)))
        return
    for i in range(N):
        if nums[i] in stack:
            continue
        stack.append(nums[i])
        backtracking(depth + 1)
        stack.pop()


backtracking(0)
