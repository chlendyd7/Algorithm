n = int(input())
nums = list(map(int,input().split()))
nums.sort()
cnt = 0

for i in range(n):
    goal = nums[i]
    left = 0
    right = n-1
    while left < right:
        mid = nums[left] + nums[right]
        if mid == goal:
            if left == i:
                left += 1
            elif right == i:
                right -= 1
            else:
                cnt += 1
                break
        elif mid > goal:
            right -= 1
        else:
            left += 1

print(cnt)
