# [0,0,1,1,1,0,1,0,1,0,1,1]	[[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]
from collections import defaultdict, deque


def solution(info, edges):
    graph = defaultdict(list)
    for a,b in edges:
        graph[a].append(b)

    answer = 0
    q = deque([(0,0,0,[])])
    while q:
        node, sheep, wolf, next_nodes = q.popleft()
        if info[node] == 0:
            sheep += 1
        else:
            wolf += 1
        
        if sheep <= wolf:
            continue

        answer = max(answer, sheep)
        next_nodes += graph[node]
        for nxt_node in next_nodes:
            q.append((nxt_node, sheep, wolf, [n for n in next_nodes if n != nxt_node]))

    return answer


def solution(info):
    from collections import deque

    n = len(info)

    graph = [[] for _ in range(n)]
    for i in range(1, n):
        parent = info[i]
        graph[parent].append(i)
    