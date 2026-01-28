import sys

def solve():
    # 모든 입력을 한 번에 읽어 split() 처리
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    inf = float('inf')
    # dist: 최단 거리 저장 / nxt: 다음 이동 노드 저장
    dist = [[inf] * (n + 1) for _ in range(n + 1)]
    nxt = [[0] * (n + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        dist[i][i] = 0
        
    idx = 2
    for _ in range(m):
        u, v, w = map(int, input_data[idx:idx+3])
        if w < dist[u][v]:
            dist[u][v] = w
            nxt[u][v] = v # u에서 v로 갈 때 첫 번째 목적지는 v
        idx += 3
        
    # 플로이드-워셜 알고리즘
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    nxt[i][j] = nxt[i][k] # i에서 j로 갈 때, 우선 i에서 k로 가는 첫 길을 따라감

    # 1. 최단 거리 행렬 출력
    for i in range(1, n + 1):
        row = []
        for j in range(1, n + 1):
            if dist[i][j] == inf:
                row.append("0")
            else:
                row.append(str(dist[i][j]))
        print(" ".join(row))
        
    # 2. 경로 정보 출력
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if dist[i][j] == 0 or dist[i][j] == inf:
                print(0)
            else:
                # 경로 추적
                path = []
                curr = i
                while curr != j:
                    path.append(curr)
                    curr = nxt[curr][j]
                path.append(j)
                
                print(len(path), " ".join(map(str, path)))

solve()