# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV15Khn6AN0CFAYD

from collections import defaultdict


def calculate(city1, city2):
    return abs(city1[0] - city2[0]) + abs(city1[1] - city2[1]) + max(0, city2[2] - city1[2])



n = int(input())
cities = [list(map(int, input().split())) for _ in range(n)]
graph = defaultdict(list)
length = len(cities)
INF = float('inf')
dp = [[INF] * n for _ in range(1<<n)]
dp[1][0] = 0

for mask in range(1<<n):
    for i in range(n):
        if dp[mask][i] == INF:
            continue
    
        for j in range(n):
            if mask & (1 << j):
                continue
            new_mask = mask | (1 << j)
            
            dp[new_mask][j] = min(dp[new_mask][j], dp[mask][i] + calculate(cities[i], cities[j]))

full_visited = (1<<n) - 1
answer = INF
for i in range(n):
    answer = min(answer, dp[full_visited][i] + calculate(cities[i], cities[0]))

print(answer)
