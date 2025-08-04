def solution():
    N, M = map(int, input().split())

    def dfs(cnt):
        if cnt == 1:
            return N

        return N * dfs(cnt - 1)

    return dfs(M)

for t in range(1, 11):
    _ = input()
    print(f'#{t} {solution()}')