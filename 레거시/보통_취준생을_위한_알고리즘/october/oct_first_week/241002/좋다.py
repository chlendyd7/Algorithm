n = int(input())
nums = list(map(int,input().split()))
nums.sort()

cnt = 0
for i in range(n):
    goal = nums[i]
    start = 0
    end = len(nums) - 1
    while start < end:
        check = nums[start] + nums[end]
        if check == goal:
            if start == i:
                start += 1
            elif end == i:
                end -= 1
            else:
                cnt += 1
                break
        elif check > goal:
            end -= 1
        elif check < goal:
            start += 1

print(cnt)