N,M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

stack = []
def backtracking(start, depth):
    if depth == M:
        print(' '.join(map(str, stack)))
        return
    
    for i in range(start, N):
        if nums[i] in stack:
            continue
        stack.append(nums[i])
        backtracking(i, depth + 1)
        stack.pop()

backtracking(0, 0)
