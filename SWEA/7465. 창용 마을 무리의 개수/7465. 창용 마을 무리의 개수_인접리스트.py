'''
    대규모 N에 적합
'''
from collections import defaultdict

def dfs(start, adj_list, visited):
    visited[start] = True
    for nxt in adj_list[start]:
        if not visited[nxt]:
            dfs(nxt, adj_list, visited)

def solution():
    N, M = map(int, input().split())
    adj_list = defaultdict(list)
    for _ in range(M):
        node1, node2 = map(int, input().split())
        adj_list[node1].append(node2)
        adj_list[node2].append(node1)

    visited = [False] * (N+1)
    cnt = 0
    for person in range(1, N+1):
        if not visited[person]:
            dfs(person, adj_list, visited)
            cnt += 1
    return cnt

T = int(input())
for t in range(1, T+1):
    print(f'#{t} {solution()}')