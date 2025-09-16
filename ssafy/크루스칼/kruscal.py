class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]

    def union(self, a, b):
        rootA, rootB = self.find(a), self.find(b)
        if rootA != rootB:
            self.parent[rootB] = rootA
            return True
        return False

def kruskal(n, edges):
    uf = UnionFind(n)
    mst_cost = 0
    mst_edges = []

    edges.sort(key=lambda x: x[2]) #(u, v, weight)

    for u, v, weight in edges:
        if uf.union(u, v):
            mst_cost += weight
            mst_edges.append((u,v,weight))
    
    return mst_cost, mst_edges

edges = [
    (0, 1, 1), (0, 2, 3), (1,2,2),
    (1,3,4), (2,3,5)
]
cost, mst = kruskal(4, edges)
print(cost, mst)
