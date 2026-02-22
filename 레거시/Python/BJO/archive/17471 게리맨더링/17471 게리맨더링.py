'''
    선거구에 포함되어 있는 구역은 모두 연결 되어야함
    인구 차이를 최소로 하려고 함

    구역의 개수 N
    1부터 N구역까지 순서대로 주어짐
    인구는 공백으로 구분되어져 있음

    그 구역과 인접한 구역의 수
    인접한 구역의 번호가 주어짐
'''
from collections import defaultdict
import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # 현재 실행 중인 파일의 절대 경로
sys.stdin = open(os.path.join(BASE_DIR, 'input.txt'), 'r')

N = int(input())
M = N//2

# 구역의 인구
populations = [0] + list(map(int, input().split()))

# 인접한 구역의 수
graph = defaultdict(list)
for i in range(N):
    graph[i+1] = list(map(int, input().split()))[1:]
print(graph)

mn = 1e9
def dfs(n, a_lst, b_lst):
    global mn
    print(n, a_lst, b_lst)
    if n == N:
        a_sum = b_sum = 0
        for idx in a_lst:
            a_sum += populations[idx]
        for idx in b_lst:
            b_sum += populations[idx]
        mn = min(mn, abs(a_sum - b_sum))
        return

    if not a_lst:
        dfs(n+1, [n], b_lst)
    if not b_lst:
        dfs(n+1, a_lst, [n])

    for value in graph[n]:
        if value in a_lst:
            dfs(n+1, a_lst + [n], b_lst)
        if value in b_lst:
            dfs(n+1, a_lst, b_lst + [n])
    else:
        return -1


dfs(1, [], [])
print(mn)

# 인접한 구역의 번호가 주어짐?