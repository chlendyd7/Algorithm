from collections import defaultdict


def solution():
    N = int(input())
    chars = [0] * (N+1)
    graph = defaultdict(list)
    for _ in range(N):
        node, word, *naver = list(input().split())
        node = int(node)
        chars[node] = word
        if naver:
            for n in naver:
                graph[node].append(int(n))
    char = ''
    def dfs(node):
        nonlocal char
        if graph[node]:
            for next in graph[node]:
                dfs(next)

        char += chars[node]
        return
    dfs(1)
    print(char)

for t in range(1, 11):
    print(f'#{t} {solution()}')