def dfs(node):
    for next in adj_list[node]:
        if visited[next]:
            continue
        visited[next] = 1
        dfs(next)

        


T = int(input())
for tc in range(1, T+1):
    answer = 0
    
    N, M = map(int, input().split())
    connections = list(map(int, input().split()))
    adj_list = [[] for _ in range(N+1)]
    visited = [0] * (N+1)

    for i in range(M):
        idx1 = i*2
        idx2 = idx1 + 1

        adj_list[connections[idx1]].append(connections[idx2])
        adj_list[connections[idx2]].append(connections[idx1])

    for node in range(1, N+1):
        if visited[node]:
            continue

        answer += 1
        visited[node] = 1
        dfs(node)
    
    print(f'#{tc} {answer}')
