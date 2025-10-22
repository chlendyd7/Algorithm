def solution():
    N = int(input())
    nums = list(map(int, input().split()))

    max_sum = sum(nums)
    dp = [False] * (max_sum + 1)
    dp[0] = True

    for p in nums:
        for s in range(max_sum, -1, -1):
            if dp[s]:
                dp[s+p] = True

    result = sum(dp)
    return result


T = int(input())
for t in range(1, T+1):
    print(f'#{t} {solution()}')