# Spanning Tree
### 그래프 내 모든 정점을 포함하는 트리
- Spanning Tree = 신장 트리 = 스패닝 트리 = 최소 연결 부분 그래프
- **원래 그래프의 일부 간선만 이용해 모든 정점을 연결하는 트리**
- **N개의 정점이 있다면 N-1개의 간선을 가짐**

```
A --- B
| \   |
|   \ |
C --- D
```
- 해당 그래프에서 스패닝 트리는 여러가지가 나올 수 있음
- A-B, B-D, D-C
- A-C, C-D, D-B

- A-B, A-C, A-D는 안됨
```
A --- B
|   /
C   D
```
C와 D는 연결되지 않았음 모든 정점 (A, B, C, D)을 연결하지 못함


## MST(Minimum Spanning Tree)
- 주어진 연결된 가중치 그래프에서 모든 정점을 연결
- 사이클이 없으면서
- 선택된 간선들의 가중치 합이 최소

총 비용이 가장 적게 드는 스패닝 트리

### MST를 찾는 방법
1. Prim 알고리즘: 한 정점에서 시작해서 점차 트리를 확장해 나가는 방식
2. Kruskal 알고리즘: 모든 간서을 짧은 순서대로 정렬한 다음 사이클이 생기지 않도록 하나씩 선택하는 방식

#### Prim 알고리즘
**확장 기반** 알고리즘: 하나의 정점에서 시작. 인접한 간선들 중에서 가장 가중치가 작은 간선을 선택해서 새로운 정점을 추가하는 방식

- 시작점 필요: 임의의 시작 정점을 선택해서 알고리즘을 시작
- Greedy방식: 매 단계에서 현재 연결된 노드들에서 가장 가중치가 낮은 간선 선택
- 우선순위 큐 활용, 우선순위 큐를 사용해서 다음으로 선택할 간선을 빠르게 찾음
- 밀집 그래프(간선이 많은 그래프)의 경우 보다 효율적
- [참조](https://8iggy.tistory.com/159)
```Python
from collections import defaultdict
import heapq
 
def mst():
    V, E = 6, 9
    edges = [[1, 2, 6], [1, 3, 3], [2, 3, 2], [2, 4, 5],
             [3, 4, 3], [3, 5, 4], [4, 5, 2], [4, 6, 3], [5, 6, 5]]
    graph = defaultdict(list)
    for srt, dst, weight in edges:
        graph[srt].append((dst, weight))
        graph[dst].append((srt, weight))
    mst_graph = [[0] * V for _ in range(V)]
    mst_nodes = [-1 for _ in range(V)]
    visited = [True for _ in range(V)]
    q = [(0, 1, 1)]
    while q:
        cost, node, prev = heapq.heappop(q)
        if visited[node - 1] is False:
            continue
        visited[node - 1] = False
        mst_graph[node - 1][prev - 1] = 1
        mst_graph[prev - 1][node - 1] = 1
        mst_nodes[node - 1] = cost
        for dst, weight in graph[node]:
            if visited[dst - 1] is True:
                heapq.heappush(q, (weight, dst, node))
    print(f'MST cost is {sum(mst_nodes)}')
    mst_graph[0][0] = 1
    for row in mst_graph:
        print(*row)
 
mst()
```

#### Kruskal 알고리즘
- **간선 기반** 알고리즘, 간선을 가중치에 따라 정렬 가장 가벼운 간선부터 차례로 MST에 추가하며 **사이클이 형성되지 않도록** 주의하며 선택
- 유니온 파인드 활용해 사이클 형성 여부를 효율적으로 확인함
- 희소 그래프(간선이 적은 그래프)의 경우 자주 사용

- [참조](https://8iggy.tistory.com/160)

##### 동작 방식 
1. 간선 정렬: 간선 가중치를 오름차순으로 정렬
2. 간선 선택 및 사이클 확인: 가중치가 작은 간선부터 하나씩 꺼냄
3. 사이클 검사: 선택된 간선이 MST에 추가되었을 대 사이클이 형성되는지 확인
    - 사이클이 형성되지 않으면 추가, 형성 된다면 버림
4. N-1개의 간선이 MST에 추가될 때까지 과정을 반복
```python
from collections import deque
 
 
def mst():
    def upward(buf, idx):
        parent = mst_nodes[idx]
        if parent < 0:
            return idx
        buf.append(idx)
        return upward(buf, parent)
 
    def find(idx):
        buf = []
        result = upward(buf, idx)
        for i in buf:
            mst_nodes[i] = result
        return result
 
    def union(x, y):
        x, y = find(x), find(y)
        if x == y:
            return False
        if mst_nodes[x] < mst_nodes[y]:
            mst_nodes[y] = x
        elif mst_nodes[x] > mst_nodes[y]:
            mst_nodes[x] = y
        else:
            mst_nodes[x] -= 1
            mst_nodes[y] = x
        return True
 
    V, E = 6, 9
    edges = [[1, 2, 6], [1, 3, 3], [2, 3, 2], [2, 4, 5],
             [3, 4, 3], [3, 5, 4], [4, 5, 2], [4, 6, 3], [5, 6, 5]]
    edges.sort(key=lambda x: x[2])
    mst_graph = [[0] * V for _ in range(V)]
    mst_nodes = [-1 for _ in range(V)]
    mst = []
    cost = 0
    q = deque(edges)
    while True:
        u, v, w = q.popleft()
        udx, vdx = u - 1, v - 1
        if union(udx, vdx) is False:
            continue
        mst.append((u, v))
        mst_graph[udx][vdx] = 1
        mst_graph[vdx][udx] = 1
        cost += w
        if len(mst) == V - 1:
            break
    print(f'mst cost is {cost}')
    print(mst)
    for row in mst_graph:
        print(*row)
 
 
mst()
```
