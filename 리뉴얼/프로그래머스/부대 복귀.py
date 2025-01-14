from collections import defaultdict


def solution(n, roads, sources, destination):
    graph = defaultdict(list)
    for a, b in roads:
        graph[a].append((b, 1))
        graph[b].append((a, 1))
        