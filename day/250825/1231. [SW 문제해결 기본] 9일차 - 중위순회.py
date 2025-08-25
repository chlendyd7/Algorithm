from collections import defaultdict


def solution():
    N = int(input())
    words = [''] * (N+1)
    graph = defaultdict()
    for _ in range(N):
        data = input().split()
        left, right = 0, 0
        node = int(data[0])
        words[node] = data[1]
        if len(data) >= 3:
            left = int(data[2])
        if len(data) >= 4:
            right = int(data[3])
        graph[node] = (left, right)

    result = ''

    def dfs(node):
        nonlocal result
        if node == 0:
            return

        left, right = graph[node]
        dfs(left)
        result += words[node]
        dfs(right)
    dfs(1)

    return result


for t in range(1, 11):
    print(f'#{t} {solution()}')