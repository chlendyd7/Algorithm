from heapq import heappop, heappush
import os
import sys


BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # 현재 실행 중인 파일의 절대 경로
sys.stdin = open(os.path.join(BASE_DIR, 'input.txt'), 'r')

V, C = map(int, input().split())
graph = [[0] * V for _ in range(V)]

for _ in range(E):
    start, end, weight = map(int, input().split())

def prim(start_node):
    pq = [(0, start_node)]
    MST = [0] * V
    min_weight = 0

    while pq:
        weight, node = heappop(pq)

        for next_node in range(V):
            if graph[node][next_node] == 0:
                continue

            if MST[node]:
                continue

            heappush(pq, (graph[node[next_node], next_node]))