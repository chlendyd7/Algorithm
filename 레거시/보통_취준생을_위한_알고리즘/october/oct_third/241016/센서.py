n = int(input())
k = int(input())
nums = list(map(int, input().split()))
nums.sort()
arr = []
for i in range(1, n):
    arr.append(nums[i] - nums[i-1])
arr.sort()
for i in range(k-1):
    arr.pop()
print(sum(arr) if arr else 0)
