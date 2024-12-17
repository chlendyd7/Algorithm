n = int(input())
cnt = 0
nums = list(map(int,input().split()))
nums.sort()

for i in nums:
    left = 0
    right = n-1
    while left<right:
        tmp = nums[left] + nums[right]
        if tmp == i:
            if left == i:
                left += 1
            elif right == i:
                right -= 1
            else:
                cnt += 1
                break
        if tmp == i:
            cnt += 1
        elif tmp < i:
            left += 1
        else:
            right -= 1
print(cnt)