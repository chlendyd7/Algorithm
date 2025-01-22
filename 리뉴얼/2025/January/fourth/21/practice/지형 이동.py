import heapq

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, rank, x, y):
    rootX = find(parent, x)
    rootY = find(parent, y)
    # if rootX != rootY:
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
    parent = [i for i in range(N*N)]
    rank = [0] * (N * N)
    
    def index(x, y):
        return x * N + y
    
    edges = []
    for x in range(N):
        for y in range(N):
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0<= nx < N and 0 <= ny < N:
                    cost = abs(land[x][y] - land[nx][ny])
                    if cost > height:
                        heapq.heappush(edges, (cost, index(x,y), index(nx, ny)))
                    else:
                        heapq.heappush(edges, (0, index(x,y), index(nx,ny)))
    
    mst_cost = 0
    while edges:
        cost, node1, node2 = heapq.heappop(edges)
        if find(parent, node1) != find(parent, node2):
            union(parent, rank, node1, node2)
            mst_cost += cost

    return mst_cost

print(solution([[1, 4, 8, 10], [5, 5, 5, 5], [10, 10, 10, 10], [10, 10, 10, 20]],3))