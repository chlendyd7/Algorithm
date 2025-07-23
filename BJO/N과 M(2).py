def backtracking(i):
    if len(result) == M:
        print(' '.join(map(str, result)))
        return

    for j in range(i, N+1):
        if not visited[j]:
            visited[j] = 1
            result.append(j)
            backtracking(j)
            result.pop()
            visited[j] = 0



N, M = map(int, input().split())
visited = [0] * (N + 1)
result = []
backtracking(1)
