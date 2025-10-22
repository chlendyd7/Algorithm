'''
1. 방문한 목록에 추가하고 다음에서 도달할 수 있는 모든 정점을 검사

ChatGPT의 말:
프림(Prim) 알고리즘은 시작 정점(인덱스) 에 따라 탐색 순서와 중간 과정은 달라질 수 있지만, 최종 결과(MST 가중치 합) 는 동일합니다.

📌 이유
프림 알고리즘은 항상 현재 선택된 정점 집합과 연결되는 가장 작은 가중치의 간선을 선택합니다.

따라서 시작점이 어디든, 최소 신장 트리(MST)의 가중치 합은 유일합니다.
(단, 같은 가중치의 간선이 여러 개일 경우 MST 자체의 구조는 여러 개가 될 수 있음)

'''
def prim(start):
    global result
    dist_array[start] = 0
    for _ in range(N):
        local_min = float('inf')
        for i in range(N):
            if visited[i] == 0 and dist_array[i] < local_min:
                min_node = i
                local_min = dist_array[i]
        visited[min_node] = 1
        result += E * local_min
    
    for j in range(N):
        if visited[j] == 0:
            tmp = (x_array[min_node] - x_array[j]) ** 2 + (y_array[min_node] - y_array[j])
            dist_array[j] = min(tmp, dist_array[j])

T = int(input())
for t in range(1, T+1):
    N = int(input())
    x_array = list(map(int, input().split()))
    y_array = list(map(int, input().split()))
    E = float(input())
    
    visited = [0] * N
    dist_array = [float('inf')] * N
    result = 0
    prim(0)
