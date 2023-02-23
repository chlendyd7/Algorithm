from collections import deque
import heapq
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    start, end, cost = map(int, input().split())
    # 간선 연결
    graph[start].append([end, cost])
    graph[end].append([start, cost])

# BFS를 이용한 풀이
def bfs(start, end):
    que = deque()
    que.append([start, 0])

    visited = [0 for _ in range(n + 1)]
    visited[start] = 1

    while que:
        # 지금 노드와 비용
        cNode, cCost = que.popleft()

        # 지금 노드가 목표 노드와 같다면 현재 축적한 비용 리턴
        if cNode == end:
            return cCost
        
        # 연결된 노드가 있다면 탐색
        for nextNode, nextCost in graph[cNode]:
            # 방문여부 확인
            if visited[nextNode] == 0:
                visited[nextNode] = 1
                que.append([nextNode, cCost + nextCost])

# 다익스트라를 이용한 풀이
def dijkstra(start, end):
    distance = [sys.maxsize] * (n + 1)
    visited = [0] * (n + 1)
    distance[start] = 0
    # 다익스트라 알고리즘은 거리가 가장 짧은 노드부터 탐색 함
    # 첫번째 인덱스를 기준으로 pop해주는 heapq의 특성을 생각해서 비용을 앞에 배치
    que = [[0, start]]

    while que:
        cost, node = heapq.heappop(que)
        if visited[node] == 1 or cost > distance[node]:
            continue
        visited[node] = 1

        for nextNode, nextCost in graph[node]:
            if visited[nextNode] == 0:
                if distance[nextNode] > distance[node] + nextCost:
                    distance[nextNode] = distance[node] + nextCost
                    heapq.heappush(que, [distance[nextNode], nextNode])

    return distance[end]
        
for _ in range(m):
    fromNode, toNode = map(int, input().split())
    # print(bfs(fromNode, toNode))
    print(dijkstra(fromNode, toNode))

[출처] [백준]Python - 1240 노드사이의 거리|작성자 Crouxi
https://blog.naver.com/mang906/222695253695