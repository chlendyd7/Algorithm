# https://atcoder.jp/contests/abc180/tasks/abc180_e
def distance(p1, p2):
    # 3D 공간에서 거리 계산: |Δx| + |Δy| + max(0, Δz)
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    return abs(x2 - x1) + abs(y2 - y1) + max(0, z2 - z1)

def solve():
    n = int(input())
    cities = [list(map(int, input().split())) for _ in range(n)]
    inf = float('inf')
    dp = [[inf] * n for _ in range(1<<n)]
    dp[1][0] = 0
    
    for mask in range(1<<n):
        for i in range(n):
            if dp[mask][i] == inf:
                continue
            
            for j in range(n):
                if mask & (1<<j):
                    continue
                
                new_mask = mask | (1 << j)
                cost = distance(cities[i], cities[j])
                dp[new_mask][j] = min(dp[new_mask][j], dp[mask][i] + cost)
    
    all_cities = (1 << n) - 1
    answer = inf
    for i in range(n):
        if dp[all_cities][i] != inf:
            answer = min(answer, dp[all_cities][i] + distance(cities[i], cities[0]))
                

    return answer
print(solve())
