# https://www.acmicpc.net/problem/20182
import heapq


def dijkstar(limit):
    dist_node = [float('inf')] * (n+1)
    dist_node[start] = 0

    pq = [(0, start)]
    while pq:
        curr, curr_node = heapq.heappop(pq)

        if dist_node[curr_node] < curr:
            continue

        if curr_node == end:
            return curr

        for neighbor, weight in graph[curr_node]:
            if weight <= limit:
                new_cost = curr + weight
                if new_cost <= budget and new_cost < dist_node[neighbor]:
                    dist_node[neighbor] = new_cost
                    heapq.heappush(pq, (curr + weight, neighbor))

    return dist_node[end]




n, m, start, end, budget = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    s, e, w = map(int, input().split())
    graph[s].append((e, w))
    graph[e].append((s, w))

s, e = 1, 20
result = -1
while s <= e:
    mid = (s+e) // 2
    if dijkstar(mid) <= budget:
        result = mid
        e = mid - 1
    else:
        s = mid + 1
print(result)
