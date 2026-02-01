import heapq
n,m, start_node, end_node, budget = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v,w))
    graph[v].append((u,w))

def dijkstra(limit):
    dist_table = [float('inf')] * (n+1)
    dist_table[start_node] = 0
    pq = [(0, start_node)]
    
    while pq:
        accumulated_cost, curr = heapq.heappop(pq)
        
        if dist_table[curr] < accumulated_cost:
            continue

        if curr == end_node:
            return accumulated_cost
        
        for neighbor, weight in graph[curr]:
            if weight <= limit:
                new_cost = accumulated_cost + weight
                if new_cost <= budget and new_cost < dist_table[neighbor]:
                    dist_table[neighbor] = new_cost
                    heapq.heappush(pq, (new_cost, neighbor))

    return dist_table[end_node]

low, high = 1, 20
answer = -1
while low <= high:
    mid = (low + high) // 2
    if dijkstra(mid) <= budget:
        answer = mid
        high = mid - 1
    else:
        low = mid + 1

print(answer)