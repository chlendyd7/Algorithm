def solution():
    N = int(input())
    nums = list(map(int, input().split()))
    cnt = 0
    total_sum = sum(nums)

    def dfs(left, right, depth, used):
        nonlocal cnt
        if depth == N:
            cnt += 1
            return

        # 가지치기: 왼쪽이 절반 이상이면 나머지 무게추 어떤 배치든 가능
        if left >= total_sum / 2:
            cnt += (2**(N - depth))
            return

        for i in range(N):
            if used[i]:
                continue
            used[i] = True
            dfs(left + nums[i], right, depth + 1, used)  # 왼쪽
            if left >= right + nums[i]:                  # 오른쪽
                dfs(left, right + nums[i], depth + 1, used)
            used[i] = False

    used = [0] * N
    dfs(0, 0, 0, used)
    return cnt


T = int(input())
for t in range(1, T + 1):
    print(f'#{t} {solution()}')
