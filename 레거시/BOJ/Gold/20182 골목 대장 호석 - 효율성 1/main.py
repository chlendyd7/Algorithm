# https://www.acmicpc.net/problem/20182
import heapq
import sys

# 입력을 빠르게 받기 위한 설정

# 1. 기본 정보 입력 (split 활용)
n, m, start_node, end_node, budget = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

def dijkstra(limit):
    """한 골목당 최대 비용이 limit 이하인 경로 중, 전체 비용 합의 최솟값 구하기"""
    # 최단 거리 테이블: 해당 노드까지 오는 데 드는 최소 전체 비용
    dist_table = [float('inf')] * (n + 1)
    dist_table[start_node] = 0
    pq = [(0, start_node)] # (누적 비용, 현재 노드)

    while pq:
        accumulated_cost, curr = heapq.heappop(pq)

        if dist_table[curr] < accumulated_cost:
            continue
        
        if curr == end_node:
            return accumulated_cost

        for neighbor, weight in graph[curr]:
            # 1. 개별 골목의 수치가 limit를 넘으면 절대 안 됨
            if weight <= limit:
                new_cost = accumulated_cost + weight
                # 2. 누적 비용이 예산(budget) 내여야 하고, 기존 경로보다 효율적이어야 함
                if new_cost <= budget and new_cost < dist_table[neighbor]:
                    dist_table[neighbor] = new_cost
                    heapq.heappush(pq, (new_cost, neighbor))
    
    return dist_table[end_node]

# 2. 이분 탐색 (골목 수치 1~20)
low, high = 1, 20
answer = -1

while low <= high:
    mid = (low + high) // 2
    # 다익스트라 결과가 예산 이내라면 (도달 가능하다면)
    if dijkstra(mid) <= budget:
        answer = mid      # 일단 정답 후보로 저장
        high = mid - 1    # 더 작은 최대 수치를 찾아봄
    else:
        low = mid + 1     # 도달 불가능하면 수치 제한을 높여봄

print(answer)
