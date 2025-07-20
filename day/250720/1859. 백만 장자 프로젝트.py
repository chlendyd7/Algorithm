def func(nums:list):
    nums = nums[::-1]
    max_value = 0
    result = 0
    for i in range(len(nums)):
        if nums[i] > max_value:
            max_value = nums[i]
            print('max_value:', max_value)
        else:
            result += (max_value - nums[i])
    return result

T = int(input())
for t in range(1, T+1):
    n = int(input())
    nums = list(map(int, input().split()))
    result = func(nums)
    print(f'#{t} {result}')
