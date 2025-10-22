# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=4&contestProbId=AWXQsLWKd5cDFAUo&categoryId=AWXQsLWKd5cDFAUo&categoryType=CODE&problemTitle=&orderBy=INQUERY_COUNT&selectCodeLang=ALL&select-1=4&pageSize=10&pageIndex=3&&&&&&&&&&
# 자신의 키가 몇 번째인지 알 수 있는 학생들 return
from collections import defaultdict, deque
'''
학생들을 노드, 키 비교를 방향 있는 간선(a < b → a → b)으로 생각한다.
모든 쌍 (i, j)에 대해 i < j 관계를 알 수 있는지 확인해야 한다.
BFS/DFS로 "i보다 큰 학생"을 탐색.
반대로 "i보다 작은 학생"도 탐색.
만약 작은 학생 수 + 큰 학생 수 == N-1 → i의 순위를 알 수 있음.
4번 학생 작은쪽 3명, 큰 쪽 2명 => N-1
'''

def bfs(start, graph, n):
    visited = [0] * (n+1)
    q = deque([start])
    visited[start] = 1
    count = 0
    while q:
        cur = q.popleft()
        for next in graph[cur]:
            if not visited[next]:
                visited[next] = 1
                q.append(next)
                count += 1
        return count


def solution():
    N = int(input()) # 학생 수
    M = int(input())

    bigger = [[] for _ in range(N+1)]
    smaller = [[] for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int, input().split())
        bigger[a].append(b)
        smaller[b].append(a)
    print('bigger:', bigger)
    print('smaller:', smaller)

    result = 0
    for i in range(1, N+1):
        big = bfs(i, bigger, N)
        small = bfs(i, smaller, N)
        if big + small == N-1:
            result += 1

    return result


T = int(input())
for t in range(1, T+1):
    print(f'#{t} {solution()}')