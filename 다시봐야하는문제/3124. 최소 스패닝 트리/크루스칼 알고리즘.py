# https://www.notion.so/chlendyd7/MST-257933ef874080688aecc86bba16afc3?source=copy_link
'''
🔹 최소 스패닝 트리(MST)
정의: 그래프의 모든 정점을 연결하면서 간선의 합이 최소가 되도록 하는 트리
조건: 사이클이 없어야 함 (트리 구조)
응용: 네트워크 설계, 배관/전선 설치 최소 비용, 군사 통신망 등

1️⃣ 크루스칼(Kruskal) 알고리즘
간선 중심 접근

단계: 
    모든 간선을 가중치 오름차순으로 정렬
    가장 작은 간선부터 사이클을 만들지 않으면 선택
    모든 정점이 연결될 때까지 반복

🔹 필요 자료 구조
유니온 파인드(Union-Find): 사이클 확인용

크루스칼 특징
    구현 간단
    간선 중심 → 간선 수가 적을 때 유리
    시간 복잡도: O(M log M) (간선 정렬)
'''

# 유니온파인드
def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a != b:
        parent[b] = a
        return True
    return False

# MST 크루스칼
def mst_kruskal(N, edges):
    edges.sort()  # 비용 오름차순 정렬
    parent = [i for i in range(N+1)]
    total = 0
    for cost, u, v in edges:
        if union(parent, u, v):
            total += cost
    return total

# 입력
N, M = map(int, input().split())
edges = []
for _ in range(M):
    u, v, cost = map(int, input().split())
    edges.append((cost, u, v))

print(mst_kruskal(N, edges))