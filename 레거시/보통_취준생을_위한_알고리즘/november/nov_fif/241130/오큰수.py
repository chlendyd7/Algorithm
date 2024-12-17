def okesu(n, nums):
    result = [-1] * n
    stack = []

    for i in range(n):
        while stack and nums[stack[-1]] < nums[i]:
            index = stack.pop()
            result[index] = nums[i]
        stack.append(i)

    return result

n = int(input())
nums = list(map(int, input().split()))

print(" ".join(map(str, okesu(n, nums))))