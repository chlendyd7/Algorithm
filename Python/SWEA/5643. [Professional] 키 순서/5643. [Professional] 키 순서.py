# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=4&contestProbId=AWXQsLWKd5cDFAUo&categoryId=AWXQsLWKd5cDFAUo&categoryType=CODE&problemTitle=&orderBy=INQUERY_COUNT&selectCodeLang=ALL&select-1=4&pageSize=10&pageIndex=3&&&&&&&&&&
# 자신의 키가 몇 번째인지 알 수 있는 학생들 return
from collections import defaultdict
'''
LCA를 사용해볼까?
dfs를 사용해야하나?
고민하다 구현 못함
'''

def solution():
    N = int(input()) # 학생 수
    M = int(input())

    graph = defaultdict(list)
    parents = {}
    for _ in range(M):
        a, b = map(int, input().split()) # a < b
        graph[b].append(a)
        parents[a] = b

        for next in graph[node]:
            cnt += dfs()
        
        return cnt
        
    cnt = 0
    for i in range(N):
        
    return


T = int(input())
for t in range(1, T+1):
    print(f'#{t} {solution()}')