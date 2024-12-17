def okensu(n, nums):
    result = []
    for i in range(n):
        found = False
        for j in range(i + 1, n):
            if nums[i] < nums[j]:
                result.append(nums[j])
                found = True
                break
        if not found:
            result.append(-1)
    return result

n = int(input())
nums = list(map(int,input().split()))
print(okensu(n,nums))
