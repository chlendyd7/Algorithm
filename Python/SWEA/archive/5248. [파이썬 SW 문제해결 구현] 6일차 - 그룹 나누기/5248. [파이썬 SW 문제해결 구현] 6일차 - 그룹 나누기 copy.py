import os
import sys


BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # 현재 실행 중인 파일의 절대 경로
sys.stdin = open(os.path.join(BASE_DIR, 'input.txt'), 'r')

# def find(x, parent):
#     if parent[x] != x:
#         return find(parent[x], parent)
#     return parent[x]

# def union(x, y, parent):
#     parent[y] = find(x, parent)

def solution():
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))
    parent = [i for i in range(N+1)]
    for i in range(0,M*2,2):
        tmp = nums[i:i+2]
        tmp.sort()
        union(tmp[0], tmp[1], parent)

    previous = [0] * (N+1)
    for i in range(1, N+1):
        previous[find(i, parent)] = 1

    return sum(previous)



T = int(input())
for t in range(1, T+1):
    print(f'#{t} {solution()}')
