from heapq import heappush, heappop


def find(parent, x):
    # 유니온-파인드의 Find 연산
    if parent[x] != x:
        parent[x] = find(parent, parent[x])  # 경로 압축
    return parent[x]


def union(parent, rank, x, y):
    # 유니온-파인드의 Union 연산 (랭크 기반)
    rootX = find(parent, x)
    rootY = find(parent, y)
    if rootX != rootY:
        if rank[rootX] > rank[rootY]:
            parent[rootY] = rootX
        elif rank[rootX] < rank[rootY]:
            parent[rootX] = rootY
        else:
            parent[rootY] = rootX
            rank[rootX] += 1


def solution(land, height):
    N = len(land)
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    parent = [i for i in range(N * N)]  # 유니온-파인드 부모 배열
    rank = [0] * (N * N)  # 유니온-파인드 랭크 배열

    def index(x, y):
        return x * N + y  # 2D 좌표를 1D 인덱스로 변환

    # 모든 간선(높이 차이와 좌표 간 연결)을 저장할 리스트
    edges = []

    # 맵을 순회하며 간선 정보를 생성
    for x in range(N):
        for y in range(N):
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < N and 0 <= ny < N:
                    cost = abs(land[x][y] - land[nx][ny])
                    if cost > height:
                        heappush(edges, (cost, index(x, y), index(nx, ny)))
                    else:
                        heappush(edges, (0, index(x, y), index(nx, ny)))

    # MST를 구성하며 최소 비용 계산
    mst_cost = 0
    while edges:
        cost, node1, node2 = heappop(edges)
        if find(parent, node1) != find(parent, node2):
            union(parent, rank, node1, node2)
            mst_cost += cost

    return mst_cost


# from heapq import heappush, heappop


# def find(parent, x):
#     # 유니온-파인드의 Find 연산
#     if parent[x] != x:
#         parent[x] = find(parent, parent[x])  # 경로 압축
#     return parent[x]


# def union(parent, rank, x, y):
#     # 유니온-파인드의 Union 연산 (랭크 기반)
#     rootX = find(parent, x)
#     rootY = find(parent, y)
#     if rootX != rootY:
#         if rank[rootX] > rank[rootY]:
#             parent[rootY] = rootX
#         elif rank[rootX] < rank[rootY]:
#             parent[rootX] = rootY
#         else:
#             parent[rootY] = rootX
#             rank[rootX] += 1


# def solution(land, height):
#     N = len(land)
#     directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
#     parent = [i for i in range(N * N)]  # 유니온-파인드 부모 배열
#     rank = [0] * (N * N)  # 유니온-파인드 랭크 배열

#     def index(x, y):
#         return x * N + y  # 2D 좌표를 1D 인덱스로 변환

#     # 모든 간선(높이 차이와 좌표 간 연결)을 저장할 리스트
#     edges = []

#     # 맵을 순회하며 간선 정보를 생성
#     for x in range(N):
#         for y in range(N):
#             for dx, dy in directions:
#                 nx, ny = x + dx, y + dy
#                 if 0 <= nx < N and 0 <= ny < N:
#                     cost = abs(land[x][y] - land[nx][ny])
#                     if cost > height:
#                         heappush(edges, (cost, index(x, y), index(nx, ny)))
#                     else:
#                         heappush(edges, (0, index(x, y), index(nx, ny)))

#     # MST를 구성하며 최소 비용 계산
#     mst_cost = 0
#     while edges:
#         cost, node1, node2 = heappop(edges)
#         print(f"Processing edge: ({node1}, {node2}) with cost {cost}")
        
#         root1 = find(parent, node1)
#         root2 = find(parent, node2)
#         print(f"Root of {node1}: {root1}, Root of {node2}: {root2}")
        
#         if root1 != root2:
#             print(f"Union nodes {node1} and {node2}")
#             union(parent, rank, node1, node2)
#             mst_cost += cost
#             print(f"Edge added to MST, current MST cost: {mst_cost}")
#         else:
#             print(f"Skipping edge ({node1}, {node2}) as it forms a cycle")

#         print(f"Parent array: {parent}")
#         print(f"Rank array: {rank}")
#         print("-" * 50)

#     return mst_cost
