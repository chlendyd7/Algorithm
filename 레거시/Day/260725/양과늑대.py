# https://school.programmers.co.kr/learn/courses/30/lessons/92343
from collections import defaultdict
def solution(info, edges):
    def dfs(node, wolf, sheep, nodes):
        nonlocal answer
        
        if info[node] == 0:
            sheep += 1
        else:
            wolf += 1
        
        if sheep <= wolf:
            return
        
        answer = max(answer, sheep)
        
        nxt_nodes = nodes + graph[node]
        for nxt_node in nxt_nodes:
            dfs(nxt_node, wolf, sheep, [n for n in nxt_nodes if n != nxt_node])
            
        
        
    graph = defaultdict(list)
    for a, b in edges:
        graph[a].append(b)
    
    answer = 0
    dfs(0, 0, 0, [])
    
    return answer