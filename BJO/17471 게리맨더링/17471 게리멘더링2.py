from itertools import combinations

# import os
# import sys

# BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # 현재 실행 중인 파일의 절대 경로
# sys.stdin = open(os.path.join(BASE_DIR, 'input.txt'), 'r')

N = int(input())
population = [0] + list(map(int, input().split()))  # 1-index
graph = [[] for _ in range(N+1)]

for i in range(1, N+1):
    data = list(map(int, input().split()))
    for j in range(1, data[0]+1):
        graph[i].append(data[j])


def is_connected(group):
    from collections import deque
    q = deque([next(iter(group))])
    visited = set([q[0]])

    while q:
        cur = q.popleft()
        for nxt in graph[cur]:
            if nxt in group and nxt not in visited:
                visited.add(nxt)
                q.append(nxt)

    return len(visited) == len(group)


ans = 1e9
area = set(range(1, N+1))

for size in range(1, N//2 + 1):
    for groupA in combinations(range(1, N+1), size):
        groupA = set(groupA)
        groupB = area - groupA

        if is_connected(groupA) and is_connected(groupB):
            popA = sum(population[i] for i in groupA)
            popB = sum(population[i] for i in groupB)
            ans = min(ans, abs(popA - popB))

print(ans if ans != 1e9 else -1)
