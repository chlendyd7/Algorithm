import sys

# 입력을 빠르게 받기 위해 sys.stdin.readline 사용 권장
input = sys.stdin.readline

n = int(input())
m = int(input())
inf = float('inf')
dist = [[inf] * (n + 1) for _ in range(n + 1)]
nxt = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    dist[i][i] = 0

for _ in range(m):
    s, e, w = map(int, input().split())
    if w < dist[s][e]:
        dist[s][e] = w
        nxt[s][e] = e  # ⭐ 놓친 부분 1: 초기 경로 설정

# 플로이드-워셜
for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]
                nxt[i][j] = nxt[i][k]

# 1. 거리 행렬 출력
for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(dist[i][j] if dist[i][j] != inf else 0, end=" ")
    print()

# 2. 경로 정보 출력
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j or dist[i][j] == inf:
            print(0)
        else:
            path = []
            curr = i
            while curr != j:
                path.append(curr)
                curr = nxt[curr][j]
            path.append(j)
            
            # ⭐ 놓친 부분 2: [개수] [경로...] 형식으로 출력
            print(len(path), *path)
