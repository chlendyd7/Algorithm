n = int(input())
result = [-1] * n
nums = list(map(int,input().split()))
stack = []

for i in range(n):
    while stack and nums[stack[-1]] < nums[i]:
        index = stack.pop()
        result[index] = nums[i]
    stack.append(i)

print(" ".join(map(str, result)))
