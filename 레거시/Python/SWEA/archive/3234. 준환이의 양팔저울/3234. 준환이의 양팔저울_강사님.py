def solution():
    N = int(input())
    nums = list(map(int, input().split()))
    cnt = 0

    def dfs(left, right, depth):
        nonlocal cnt
        if depth == N:
            cnt += 1
            return

        if left >= total_sum // 2:
            cnt += (2**(N-depth))
            return

        for i in range(N):
            if visited[i]:
                continue
            visited[i] = True
            dfs(left + nums[i], right, depth+1)
            if left >= right + nums[i]:
                dfs(left, right + nums[i], depth + 1)

            visited[i] = False

    visited = [0] * N
    total_sum = sum(nums)
    dfs(0, 0, 0, visited)
    return cnt

T = int(input())
for t in range(1, T+1):
    print(f'#{t} {solution()}')