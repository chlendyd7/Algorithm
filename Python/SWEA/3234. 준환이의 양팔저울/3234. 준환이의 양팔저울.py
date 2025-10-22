def solution():
    N = int(input())
    nums = list(map(int, input().split()))
    cnt = 0

    def dfs(left, right, depth, used):
        nonlocal cnt
        if depth == N:
            cnt += 1
            return

        if left >= total_sum // 2:
            cnt += (2**(N-depth))
            return

        for i in range(N):
            if used[i]:
                continue
            used[i] = True
            dfs(left + nums[i], right, depth+1, used)
            if left >= right + nums[i]:
                dfs(left, right + nums[i], depth + 1, used)

            used[i] = False

    used = [0] * N
    total_sum = sum(nums)
    dfs(0, 0, 0, used)
    return cnt

T = int(input())
for t in range(1, T+1):
    print(f'#{t} {solution()}')