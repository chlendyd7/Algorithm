# https://atcoder.jp/contests/abc180/tasks/abc180_e
'''
mask & (1 << j)

"mask에서 위치 j가 1인가?"

'''
def distance(p1, p2):
    # 3D 공간에서 거리 계산: |Δx| + |Δy| + max(0, Δz)
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    return abs(x2 - x1) + abs(y2 - y1) + max(0, z2 - z1)


def solve():
    # 입력받기
    N = int(input())
    cities = []
    for _ in range(N):
        x, y, z = map(int, input().split())
        cities.append((x, y, z))
    
    # DP 배열: dp[mask][i] = mask 상태에서 도시 i에 있을 때의 최소 비용
    INF = float('inf')
    dp = [[INF] * N for _ in range(1 << N)]
    dp[1][0] = 0  # 시작: 도시 0에서 출발
    
    # 모든 상태에서 미방문 도시로 이동하며 DP 계산
    for mask in range(1 << N):
        for i in range(N):
            if dp[mask][i] == INF:
                continue
            
            # 미방문 도시 j로 이동
            for j in range(N):
                if mask & (1 << j):  # 이미 방문했으면 스킵
                    continue
                
                new_mask = mask | (1 << j)  # 도시 j 방문 표시
                cost = distance(cities[i], cities[j])
                dp[new_mask][j] = min(dp[new_mask][j], dp[mask][i] + cost)
    
    # 모든 도시 방문 후 시작점으로 복귀
    all_visited = (1 << N) - 1
    answer = INF
    for i in range(N):
        if dp[all_visited][i] != INF:
            answer = min(answer, dp[all_visited][i] + distance(cities[i], cities[0]))
    
    return answer


print(solve())
