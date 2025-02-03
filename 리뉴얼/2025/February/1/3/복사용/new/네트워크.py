from collections import deque


def solution(n, computers):
    def dfs(node):
        visited[node] = True
        for i, connected in enumerate(computers[node]):
            if connected == 1 and not visited[i]:
                dfs(i)

    visited = [False] * n
    count = 0
    for i in range(n):
        if not visited[i]:
            dfs(i)
            count += 1

    return counts