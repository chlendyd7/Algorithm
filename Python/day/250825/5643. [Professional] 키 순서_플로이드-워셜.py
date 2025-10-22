def solution():
    N = int(input())
    M = int(input())
    
    graph = [[0] * (N+1) for _ in range(N+1)]

    for _ in range(M):
        a, b = map(int, input().split())
        graph[a][b] = 1

    for k in range(1, N+1):
        for i in range(1, N+1):
            for j in range(1, N+1):
                if graph[i][k] and graph[k][j]:
                    graph[i][j] = 1

    result = 0
    for i in range(1, N+1):
        bigger = sum(graph[i])
        smaller = sum(graph[j][i] for j in range(1, N+1))
        if bigger + smaller == N-1:
            result += 1

T = int(input())
for t in range(1, T+1):
    print(f'#{t} {solution()}')