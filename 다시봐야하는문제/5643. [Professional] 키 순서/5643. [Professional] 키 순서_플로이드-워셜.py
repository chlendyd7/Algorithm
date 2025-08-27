'''
Floyd-Warshall이란?

모든 정점 쌍 사이의 최단 경로를 구하는 알고리즘

다이나믹 프로그래밍(DP) 기반

시간복잡도: O(N^3)

음수 가중치가 있어도 동작(단, 음수 사이클이 있으면 안 됨)

즉, "A → B로 가는 최단 경로가 있는가? 그 비용은 얼마인가?" 를 모든 쌍에 대해 한 번에 구할 수 있어.
'''

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    M = int(input())
    
    # 인접 행렬 (0: 모름, 1: i<j)
    graph = [[0]*(N+1) for _ in range(N+1)]

    for _ in range(M):
        a, b = map(int, input().split())
        graph[a][b] = 1   # a < b

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

