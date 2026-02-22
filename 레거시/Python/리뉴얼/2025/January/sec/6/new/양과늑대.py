from collections import defaultdict, deque


def solution(info, edges):
    graph = defaultdict(list)
    for parent, child in edges:
        graph[parent].append(child)
    
    max_sheep= 0
    q = deque([(0, 0, 0, [])])

    while q:
        current, sheep, wolves, next_nodes = q.popleft()

        if info[current] == 0:
            sheep += 1
        else:
            wolves += 1
        
        if sheep <= wolves:
            continue
            
        max_sheep = max(max_sheep, sheep)

        next_nodes = next_nodes + graph[current]
        for next_node in next_nodes:
            q.append((next_node, sheep, wolves, [n for n in next_node if n != next_node]))

    
    return max_sheep