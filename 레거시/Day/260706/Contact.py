# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV15B1cKAKwCFAYD

from collections import defaultdict, deque

def solution():
    n, s = map(int, input().split())
    inputs = list(map(int, input().split()))
    graph = defaultdict(list)
    for i in range(0, n, 2):
        graph[inputs[i]].append(inputs[i+1])

    q = deque(graph[s])

    check = []
    visited = [s]
    cnt = 0
    while q:
        cnt += 1
        for i in range(len(q)):
            now = q.popleft()    
            for next in graph[now]:
                if next not in visited:
                    visited.append(next)
                    q.append(next)
                    check.append((cnt+1, next))
    check.sort(key=lambda x: [x[0], x[1]])
    return check[0][1]

for t in range(1, 11):
    print(f'{t} {solution()}')




from collections import defaultdict, deque

def solution():
    # split()을 활용한 입력 받기
    n, s = map(int, input().split())
    inputs = list(map(int, input().split()))
    
    graph = defaultdict(list)
    for i in range(0, n, 2):
        graph[inputs[i]].append(inputs[i+1])
    
    # visited 배열을 0으로 초기화 (0은 미방문, 숫자는 방문 차수)
    visited = [0] * 101
    
    q = deque([s])
    visited[s] = 1 # 시작점 방문 표시 (1번째 단계)
    
    while q:
        now = q.popleft()
        
        for next_node in graph[now]:
            # 아직 방문하지 않은 노드라면
            if visited[next_node] == 0:
                # 이전 노드의 방문 차수 + 1을 저장
                visited[next_node] = visited[now] + 1
                q.append(next_node)
    
    # 모든 탐색이 끝난 후, visited 배열에서 가장 큰 차수(가장 나중)를 찾고
    # 그 중 인덱스(번호)가 가장 큰 값을 구합니다.
    max_turn = max(visited)
    max_node = 0
    
    for i in range(101):
        if visited[i] == max_turn:
            max_node = i
            
    return max_node

for t in range(1, 11):
    print(f'#{t} {solution()}')