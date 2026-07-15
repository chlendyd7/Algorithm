from collections import defaultdict, deque

# [0,0,1,1,1,0,1,0,1,0,1,1]
# [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]
def solution(info, edges):
    graph = defaultdict(list)
    for a, b in edges:
        graph[a].append(b)

    now_node = 0

    answer = 0
    # start, sheep, wolf, next[]
    q = deque([(0, 1, 0, [])])
    while q:
        node, sheep, wolf, next = q.popleft()
        for nxt in graph[node]:
            


    return answer