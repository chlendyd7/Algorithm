from collections import defaultdict


def solution(n, edges):
    graph = defaultdict(list)
    for a,b in edges:
        graph[a].append(b)
        graph[b].append(a)
    print(graph)
    answer = 0
    return answer