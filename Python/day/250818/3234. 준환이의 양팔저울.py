


from itertools import permutations


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    numbers = list(map(int, input().split()))
    answer = 0
    total = sum(numbers)

    def dfs(left, right, depth, p):
        global answer
        if depth == N:
            answer += 1
            return

        now = p[depth]
        
        if left > (total // 2):
            answer + 2 ** (N - depth)
            return

        elif left >= (right + now):
            dfs(left, right + now, depth + 1, perm)
            dfs(left + right, right, depth + 1, perm)
        else:
            dfs(left + now, right, depth + 1, perm)

    for perm in permutations(numbers, N):
        dfs(0, 0, 0, perm)

    print(f"#{test_case} {answer}")
