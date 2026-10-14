# https://school.programmers.co.kr/learn/courses/30/lessons/92343
from collections import defaultdict, deque


def solution(info, edges):
    graph = defaultdict(list)
    for a, b in edges:
        graph[a].append(b)
    
    answer = 0
    
    def dfs(node, sheep, wolf, nxt):
        nonlocal answer
        if info[node] == 0:
            sheep += 1
        elif info[node] == 1:
            wolf += 1

        if sheep <= wolf:
            return
        
        answer = max(answer, sheep)

        nxt += graph[node]
        for next_node in nxt:
            dfs(next_node, sheep, wolf, [n for n in nxt if n != next_node])
    dfs(0, 0, 0, [])

    return answer

print(solution([0,0,1,1,1,0,1,0,1,0,1,1],[[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]))
