'''
    인접 행렬(N이 작은 경우)
'''
def dfs(start, adj_matrix, visited):
    visited[start] = True
    for next in range(1, len(adj_matrix)):
        if adj_matrix[start][next] and not visited[next]:
            dfs(next, adj_matrix, visited)

def solution():
    N, M = map(int, input().split())
    adj_matrix = [[0] * (N+1) for _ in range(N+1)]
    for _ in range(M):
        node1, node2 = map(int, input().split())
        adj_matrix[node1][node2] = 1
        adj_matrix[node2][node1] = 1

    visited = [False] * (N+1)
    cnt = 0
    for person in range(1, N+1):
        if not visited[person]:
            dfs(person, adj_matrix, visited)
            cnt += 1
    return cnt


T = int(input())
for t in range(1, T+1):
    print(f'#{t} {solution()}')
