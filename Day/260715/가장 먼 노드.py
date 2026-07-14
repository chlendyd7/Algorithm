# https://school.programmers.co.kr/learn/courses/30/lessons/49189
from collections import defaultdict
import heapq
INF = 10**18
def solution(n, edge):
    distance = [INF] * (n+1)
    graph = defaultdict(list)
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
    
    hq = [(0,1)]
    distance[1] = 0
    while hq:
        v, node = heapq.heappop(hq)
        if distance[node] < v:
            continue
        
        for nxt in graph[node]:
            nxt_value = v + 1
            if distance[nxt] > nxt_value:
                distance[nxt] = nxt_value
                heapq.heappush(hq, (nxt_value, nxt))
    
    mx = max(distance[1:])
    return sum(1 for d in distance if d == mx)


네, 맞습니다! 이 문제는 1번 노드에서 다른 모든 노드까지의 최단 경로를 구하는 문제이기 때문에 **다익스트라(Dijkstra) 알고리즘**으로 해결할 수 있습니다.

다만, 작성하신 코드에 아주 결정적인 논리적 오류(버그)가 하나 있어서 모든 노드의 거리가 업데이트되지 않고 `INF`로 남아있던 것입니다.

---

## 🔍 기존 코드의 버그 분석

작성하신 코드의 20~21라인을 보면 다음과 같이 되어 있습니다.

```python
for nxt in graph[node]:
    nxt_value = v + 1
    if distance[node] > nxt_value:        # ❌ 오류!
        distance[node] = nxt_value        # ❌ 오류!
        heapq.heappush(hq, (nxt_value, nxt))

```

* **원인:** 다음 노드(`nxt`)로 가는 최단 거리를 갱신해야 하므로 `distance[nxt]`를 비교하고 업데이트해야 하는데, 현재 탐색 중인 노드인 `distance[node]`를 비교하고 수정하고 있습니다.
* **해결:** `distance[node]` 대신 `distance[nxt]`로 변경해야 합니다.

---

## 🛠️ 올바른 다익스트라 코드 예시

오류를 수정하고, 1번 노드로부터 가장 먼 노드(최대 거리)의 개수를 구하는 마무리 로직까지 추가한 코드입니다.

```python
from collections import defaultdict
import heapq

INF = 10**18

def solution(n, edge):
    distance = [INF] * (n + 1)
    graph = defaultdict(list)
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
    
    hq = [(0, 1)]
    distance[1] = 0
    while hq:
        v, node = heapq.heappop(hq)
        if distance[node] < v:
            continue
        
        for nxt in graph[node]:
            nxt_value = v + 1
            # 💡 distance[node]가 아닌 distance[nxt]를 비교하고 갱신해야 합니다!
            if distance[nxt] > nxt_value:
                distance[nxt] = nxt_value
                heapq.heappush(hq, (nxt_value, nxt))
    
    # 1번 노드를 제외한 노드들 중 가장 먼 거리 찾기
    valid_distances = distance[2:] # 0번(사용 안 함), 1번(시작 노드이므로 거리 0) 제외
    max_dist = max(valid_distances)
    
    # 가장 먼 거리와 같은 값을 가진 노드의 개수 반환
    return valid_distances.count(max_dist)

```

---

## 💡 더 좋은 방법 추천: BFS (너비 우선 탐색)
'''

이 문제처럼 **모든 간선의 가중치가 1로 동일할 때**는 다익스트라($O(E \log V)$)보다 BFS($O(V + E)$)를 사용하는 것이 훨씬 더 빠르고 효율적입니다. 우선순위 큐(`heapq`)를 유지하는 비용이 들지 않기 때문입니다.

`collections.deque`를 활용한 간단하고 정석적인 BFS 풀이도 함께 참고해 보세요!

```python

'''
from collections import deque, defaultdict

def solution(n, edge):
    graph = defaultdict(list)
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
        
    # 방문 여부 및 거리를 기록할 배열 (-1로 초기화)
    visited = [-1] * (n + 1)
    
    # 1번 노드 시작 설정
    queue = deque([1])
    visited[1] = 0
    
    while queue:
        curr = queue.popleft()
        
        for nxt in graph[curr]:
            # 아직 방문하지 않은 노드라면 현재 거리 + 1로 방문 처리
            if visited[nxt] == -1:
                visited[nxt] = visited[curr] + 1
                queue.append(nxt)
                
    # 가장 먼 거리 찾기
    max_dist = max(visited)
    
    # 가장 먼 거리에 있는 노드의 개수 세기
    return visited.count(max_dist)
