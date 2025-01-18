from collections import deque
import heapq


def solution(land, height):
    N = len(land)
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    
    # 1. 영역 구분
    def bfs(start_x, start_y, zone_id):
        queue = deque([(start_x, start_y)])
        zones[start_x][start_y] = zone_id
        while queue:
            x, y = queue.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < N and 0 <= ny < N and zones[nx][ny] == -1:
                    if abs(land[nx][ny] - land[x][y]) <= height:  # 이동 가능
                        zones[nx][ny] = zone_id
                        queue.append((nx, ny))

    # 2. MST를 위한 간선 정보 생성
    def find_edges():
        edges = []
        for x in range(N):
            for y in range(N):
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < N and 0 <= ny < N:
                        if zones[x][y] != zones[nx][ny]:  # 다른 영역 연결
                            cost = abs(land[x][y] - land[nx][ny])
                            edges.append((cost, zones[x][y], zones[nx][ny]))
        return edges

    # 3. 유니온-파인드 알고리즘
    def find(parent, x):
        if parent[x] != x:
            parent[x] = find(parent, parent[x])
        return parent[x]

    def union(parent, rank, x, y):
        root_x = find(parent, x)
        root_y = find(parent, y)
        if root_x != root_y:
            if rank[root_x] > rank[root_y]:
                parent[root_y] = root_x
            elif rank[root_x] < rank[root_y]:
                parent[root_x] = root_y
            else:
                parent[root_y] = root_x
                rank[root_x] += 1

    # 영역 구분
    zones = [[-1] * N for _ in range(N)]
    zone_id = 0
    for i in range(N):
        for j in range(N):
            if zones[i][j] == -1:
                bfs(i, j, zone_id)
                zone_id += 1

    # MST 구성
    edges = find_edges()
    edges.sort()

    # 유니온-파인드 초기화
    parent = [i for i in range(zone_id)]
    rank = [0] * zone_id

    # 크루스칼 알고리즘
    total_cost = 0
    for cost, zone_a, zone_b in edges:
        if find(parent, zone_a) != find(parent, zone_b):
            union(parent, rank, zone_a, zone_b)
            total_cost += cost

    return total_cost
