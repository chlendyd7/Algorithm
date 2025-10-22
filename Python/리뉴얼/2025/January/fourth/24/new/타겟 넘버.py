from collections import defaultdict
import heapq


def solution(tickets):
    root = defaultdict(list)
    for ticket in tickets:
        heapq.heappush(root[ticket[0]], ticket[1])
    print(root)
    answer = []
    def dfs(start):
        answer.append(start)
        next = heapq.heappop(root[start])
        dfs(next)
    dfs('ICN')
    return answer