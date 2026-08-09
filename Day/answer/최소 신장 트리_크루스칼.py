#https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWUS26fKIucDFAVT&categoryId=AWUS26fKIucDFAVT&categoryType=CODE&problemTitle=%EC%B5%9C%EC%86%8C+%EC%8B%A0%EC%9E%A5+%ED%8A%B8%EB%A6%AC&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1



def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    root_a = find(parent, a)
    root_b = find(parent, b)
    
    if root_a < root_b:
        parent[root_b] = root_a
    else:
        parent[root_a] = root_b

T = int(input())
for t in range(1, T + 1):
    V, E = map(int, input().split())
    edges = []
    
    # E개의 간선 정보를 입력받음
    for _ in range(E):
        u, v, w = map(int, input().split())
        edges.append((w, u, v))
    
    # 가중치(w) 기준으로 오름차순 정렬
    edges.sort()
    
    # 0번부터 V번까지 노드의 부모 배열 초기화
    parent = [i for i in range(V + 1)]
    
    total_weight = 0
    cnt = 0
    
    for w, u, v in edges:
        # 두 노드의 대표 부모가 다르면(사이클이 생기지 않으면) 선택
        if find(parent, u) != find(parent, v):
            union(parent, u, v)
            total_weight += w
            cnt += 1
            if cnt == V:  # 노드가 (V+1)개이므로 간선 V개를 선택하면 MST 완성
                break
    
    print(f'#{t} {total_weight}')