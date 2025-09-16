from heapq import heappop, heappush
import os
import sys


BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # 현재 실행 중인 파일의 절대 경로
sys.stdin = open(os.path.join(BASE_DIR, 'input.txt'), 'r')

V, C = map(int, input().split())
graph = [[0] * V for _ in range(V)]

edges = []
for _ in range(E):
    start, end, weight = map(int, input().split())
    edges.append((start, end, weight))

edges.sort(key=lambda x: x[2])

cnt = 0
result = 0
def find_set(x):
    if x == parents[x]:
        parents[x] = find_set(parents[x])
    return parents[x]

def union(x,y):
    rx = find_set(x)
    ry = find_set(y)

    if rx == ry:
        return
    if rx < ry:
        parents[ry] = rx
    else:
        parents[rx] = ry


parents = [i for i in range(V)]
for u, v, w in edges:
    if find_set(u) != find_set(v):
        union(u, v)
        cnt += 1
        result += w

    if cnt == V-1:
        break

print(f'최소 비용 = {result}')
