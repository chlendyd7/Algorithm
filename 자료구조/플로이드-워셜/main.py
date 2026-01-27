'''
점화식 $$dist[i][j] = \min(dist[i][j], dist[i][k] + dist[k][j])$$
플로이드-워셜은 $3$중 for문을 사용하므로 시간 복잡도가 $O(N^3)$입니다. 노드 개수($N$)가 500개인 위 문제(11657번)에 적용하면 $500^3 = 125,000,000$으로 시간 초과가 날 가능성이 높지만, 일반적인 최단 거리 문제에서는 매우 유용합니다.

구분,벨만-포드 (Bellman-Ford),플로이드-워셜 (Floyd-Warshall)
목적,한 지점 → 모든 지점,모든 지점 → 모든 지점
시간 복잡도,O(VE),O(N3)
음수 가중치,가능 (음수 사이클 감지 가능),"가능 (단, 음수 사이클이 없어야 함)"
추천 상황,N이 크고 시작점이 정해져 있을 때,N이 작고(보통 400 이하) 모든 경로가 필요할 때
'''



def floyd_warshall():
    n = int(input())
    m = int(input())
    inf = float('inf')
    graph = [[inf] * (n+1) for _ in range(n+1)]
    
    for i in range(1, n+1):
        graph[i][i] = 0
    
    idx = 2
    for _ in range(m):
        u, v, w = map(int, input().split())
        graph[u][v] = min(graph[u][v], w)
        idx += 3
    
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if graph[i][k] + graph[k][j] < graph[i][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]
    
    for i in range(1, n+1):
        for j in range(1, n+1):
            if graph[i][j] == inf:
                print("INF", end=' ')
            else:
                print(graph[i][j], end=' ')
            print()

floyd_warshall()
