'''
N개의 구역으로 나누어짐
2개의 선거구로 나눠야함 각 구역은 두 개의 선거구 중 하나에 포함

같은 선거구 모두 연결되야함

input N <= 10 완탐
N개의 구역
구역의 인구 1 ~ N 까지
N개의 줄에 각 구역과 인접한 구역의 정보가 주어짐


output: 각 선거구에 포함된 인구의 차이를 최소로
'''

import sys
from collections import deque
MAX = sys.maxsize
input = sys.stdin.readline


N = int(input())
n = int(input())
arr = [0] + list(map(int, input().split()))
graph = [[] for _ in range(n + 1)]

# 그래프 생성
for i in range(1, n + 1):
    t = list(map(int, input().split()))
    graph[i].extend(t[1:])
